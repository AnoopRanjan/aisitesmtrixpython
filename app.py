#!/usr/bin/env python3
"""
AI Tools Explorer - Python Web Application
===========================================
A high-performance, zero-dependency Python web application serving interactive
tabs, single-paragraph tool breakdowns, and embedded YouTube videos for the 9 AI tools.

Usage:
    python app.py [--port PORT] [--host HOST] [--no-browser]
"""

import sys
import os
import json
import argparse
import socket
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

from tools_data import TOOLS_DATA

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Multi-threaded HTTP Server for smooth concurrent request handling."""
    daemon_threads = True
    allow_reuse_address = True


class AIToolsRequestHandler(SimpleHTTPRequestHandler):
    """Custom HTTP Request Handler serving Web UI and JSON API endpoints."""

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split("?")[0].rstrip("/")

        # Route 1: Home page / Index
        if clean_path in ("", "/index.html", "/home"):
            self.serve_index()
            return

        # Route 2: API all tools
        elif clean_path == "/api/tools":
            self.serve_json(TOOLS_DATA)
            return

        # Route 3: API single tool by ID
        elif clean_path.startswith("/api/tools/"):
            tool_id = clean_path.replace("/api/tools/", "").strip()
            match = next((t for t in TOOLS_DATA if t["id"] == tool_id), None)
            if match:
                self.serve_json(match)
            else:
                self.serve_error(404, f"Tool '{tool_id}' not found.")
            return

        # Route 4: Health check
        elif clean_path == "/health":
            self.serve_json({"status": "ok", "tools_count": len(TOOLS_DATA)})
            return

        # Route 5: Static files
        else:
            file_path = os.path.join(BASE_DIR, self.path.lstrip("/"))
            if os.path.exists(file_path) and os.path.isfile(file_path):
                super().do_GET()
            else:
                # Fallback to index.html for SPA-style client routing
                self.serve_index()

    def serve_index(self):
        """Serve the index.html page."""
        try:
            with open(INDEX_FILE, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.serve_error(500, f"Error loading index.html: {str(e)}")

    def serve_json(self, data):
        """Serve JSON response."""
        encoded = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def serve_error(self, code, message):
        """Serve JSON error response."""
        error_payload = json.dumps({"error": message, "code": code}).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(error_payload)))
        self.end_headers()
        self.wfile.write(error_payload)

    def log_message(self, format, *args):
        """Cleaner log formatting."""
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")


def find_free_port(start_port=5000, max_attempts=50):
    """Find the next available port if start_port is occupied."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return start_port


def start_server(host="127.0.0.1", port=5000, open_browser=True):
    """Start the AI Tools web server."""
    actual_port = find_free_port(port)
    server_address = (host, actual_port)
    httpd = ThreadedHTTPServer(server_address, AIToolsRequestHandler)

    url = f"http://{host}:{actual_port}"
    print("=" * 70)
    print(" 🚀 AI POWER TOOLS EXPLORER - PYTHON APPLICATION")
    print("=" * 70)
    print(f" Web Server Running at : {url}")
    print(f" REST API Endpoint     : {url}/api/tools")
    print(f" Total Tools Tracked   : {len(TOOLS_DATA)}")
    print(" Press Ctrl+C in this console to stop the server.")
    print("=" * 70)

    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down server gracefully...")
        httpd.shutdown()
        print("[+] Server stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the AI Tools Explorer Web Application.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on (default: 5000)")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically launch web browser")
    args = parser.parse_args()

    start_server(host=args.host, port=args.port, open_browser=not args.no_browser)
