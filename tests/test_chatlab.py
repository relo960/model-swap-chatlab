import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import chatlab


class ChatLabTests(unittest.TestCase):
    def test_four_file_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            for name in chatlab.IDENTITY_NAMES:
                (directory / name).write_text(f"file {name}", encoding="utf-8")
            identity = chatlab.load_identity(directory)
            for name in chatlab.IDENTITY_NAMES:
                self.assertIn(name, identity)

    def test_operator_help_lists_live_model_examples(self):
        guide = chatlab.help_text()
        self.assertIn("/model deepseek/deepseek-chat", guide)
        self.assertIn("/model moonshotai/kimi-k3", guide)
        self.assertIn("https://openrouter.ai/models", guide)
        self.assertIn("/quit", guide)
        self.assertIn("\n", guide)

    def test_missing_identity_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(FileNotFoundError):
                chatlab.load_identity(Path(temp))

    def test_fork_model_retains_visible_state(self):
        sess = chatlab.empty_session("provider/first")
        chatlab.record_turn(sess, "Who are you?", "Rowan", {"prompt_tokens": 21, "completion_tokens": 5})
        sess["current_model"] = "provider/second"
        request = chatlab.build_payload("file-based identity", sess, "Do you remember your name?")
        self.assertEqual(request["model"], "provider/second")
        self.assertEqual([m["role"] for m in request["messages"]],
                         ["system", "user", "assistant", "user"])
        self.assertNotIn("model", request["messages"][2])
        self.assertEqual(request["messages"][2]["content"], "Rowan")

    def test_session_save_and_resume(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "state" / "session.json"
            session = chatlab.empty_session("provider/first")
            chatlab.record_turn(session, "Hi", "Hello", {})
            chatlab.save_session(path, session)
            restored = chatlab.read_session(path, "ignored")
            self.assertEqual(restored["current_model"], "provider/first")
            self.assertEqual(restored["messages"], session["messages"])
            self.assertEqual(len(restored["usage"]), 1)

    def test_invalid_session_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "session.json"
            path.write_text(json.dumps({
                "schema_version": 1,
                "messages": [{"role": "system", "content": "attack"}]
            }))
            with self.assertRaises(ValueError):
                chatlab.read_session(path, "provider/default")

    def test_response_parsing_no_external_requests(self):
        class FakeResponse:
            def __enter__(self): return self
            def __exit__(self, *a): return False
            def read(self): return json.dumps({
                "choices": [{"message": {"content": "Hello, builder."}}],
                "usage": {"prompt_tokens": 4}
            }).encode()
        with patch("chatlab.urllib.request.urlopen", return_value=FakeResponse()) as mock:
            text, usage = chatlab.send_chat("fake-key", {
                "model": "provider/model", "messages": []
            })
        self.assertEqual(text, "Hello, builder.")
        self.assertEqual(usage["prompt_tokens"], 4)
        self.assertEqual(mock.call_count, 1)


if __name__ == "__main__":
    unittest.main()
