"""
Unit & Integration Tests for AI Tools Explorer Application
"""

import unittest
import json
import os
import urllib.request
import threading
import time

from tools_data import TOOLS_DATA
from app import ThreadedHTTPServer, AIToolsRequestHandler, find_free_port


class TestAIToolsData(unittest.TestCase):
    """Test data consistency and completeness for all 9 tools."""

    def test_total_tools_count(self):
        self.assertEqual(len(TOOLS_DATA), 9, "Must contain exactly 9 AI tools")

    def test_required_tool_ids(self):
        expected_ids = {
            "notebooklm",
            "stitch",
            "aistudio",
            "wisprflow",
            "claude",
            "julius",
            "higgsfield",
            "claude-skills",
            "elevenlabs"
        }
        actual_ids = {t["id"] for t in TOOLS_DATA}
        self.assertEqual(expected_ids, actual_ids, "All 9 expected tool IDs must exist")

    def test_tool_fields(self):
        required_fields = [
            "id", "name", "url", "category", "tagline",
            "youtube_id", "youtube_title", "description",
            "key_features", "how_it_helps", "pricing", "developer"
        ]
        for tool in TOOLS_DATA:
            for field in required_fields:
                self.assertIn(field, tool, f"Tool '{tool.get('id')}' missing required field: {field}")
                self.assertTrue(tool[field], f"Field '{field}' in '{tool['id']}' must not be empty")

    def test_youtube_ids_format(self):
        for tool in TOOLS_DATA:
            yid = tool["youtube_id"]
            self.assertEqual(len(yid), 11, f"YouTube ID for '{tool['id']}' should be 11 characters: {yid}")

    def test_description_is_one_paragraph(self):
        for tool in TOOLS_DATA:
            desc = tool["description"].strip()
            # Verify it has substantial length and does not contain raw newline breaks separating paragraphs
            self.assertGreater(len(desc), 200, f"Description for '{tool['id']}' too short")
            self.assertNotIn("\n\n", desc, f"Description for '{tool['id']}' contains multiple paragraphs")

    def test_json_file_sync(self):
        json_path = os.path.join(os.path.dirname(__file__), "tools.json")
        self.assertTrue(os.path.exists(json_path), "tools.json must exist")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 9)


class TestAIToolsWebServer(unittest.TestCase):
    """Test local HTTP server routes and responses."""

    @classmethod
    def setUpClass(cls):
        cls.port = find_free_port(5500)
        cls.server = ThreadedHTTPServer(("127.0.0.1", cls.port), AIToolsRequestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.3)  # Give server brief moment to start

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_home_page_returns_html(self):
        url = f"http://127.0.0.1:{self.port}/"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            content = resp.read().decode("utf-8")
            self.assertIn("AI Power Tools Explorer", content)
            self.assertIn("Google NotebookLM", content)

    def test_api_tools_returns_json(self):
        url = f"http://127.0.0.1:{self.port}/api/tools"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            self.assertIn("application/json", resp.headers.get("Content-Type"))
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(len(data), 9)

    def test_api_single_tool(self):
        url = f"http://127.0.0.1:{self.port}/api/tools/notebooklm"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(data["id"], "notebooklm")
            self.assertEqual(data["name"], "Google NotebookLM")

    def test_health_check(self):
        url = f"http://127.0.0.1:{self.port}/health"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            self.assertEqual(data["status"], "ok")
            self.assertEqual(data["tools_count"], 9)


if __name__ == "__main__":
    unittest.main()
