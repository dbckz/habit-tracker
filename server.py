#!/usr/bin/env python3
"""
Simple Habit Tracker Server
Serves the web app and persists habit data to a local JSON file.

Usage:
    python server.py
    
Then open http://localhost:8765 in your browser.
"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 8766
DATA_FILE = Path(__file__).parent / "habits.json"


class HabitTrackerHandler(SimpleHTTPRequestHandler):
    """Custom handler for serving files and handling API requests."""
    
    def __init__(self, *args, **kwargs):
        # Serve files from the same directory as this script
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/api/habits":
            self.send_json_response(load_habits())
        elif self.path == "/" or self.path == "":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()
    
    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/api/habits":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            
            try:
                habits = json.loads(body.decode("utf-8"))
                save_habits(habits)
                self.send_json_response({"status": "ok"})
            except json.JSONDecodeError:
                self.send_error_response(400, "Invalid JSON")
            except Exception as e:
                self.send_error_response(500, str(e))
        else:
            self.send_error_response(404, "Not found")
    
    def send_json_response(self, data, status=200):
        """Send a JSON response."""
        response = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(response))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response)
    
    def send_error_response(self, status, message):
        """Send an error response."""
        self.send_json_response({"error": message}, status)
    
    def log_message(self, format, *args):
        """Quieter logging - only show errors."""
        if args[1][0] not in ("2", "3"):  # Not 2xx or 3xx
            super().log_message(format, *args)


def load_habits():
    """Load habits from the JSON file."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_habits(habits):
    """Save habits to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, indent=2, ensure_ascii=False)


def main():
    """Start the server."""
    server = HTTPServer(("localhost", PORT), HabitTrackerHandler)
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║              🌱 Habit Tracker Server                     ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   Open in your browser:  http://localhost:{PORT}          ║
║                                                          ║
║   Data saved to: {DATA_FILE.name:<25}           ║
║                                                          ║
║   Press Ctrl+C to stop the server                        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped. Your habits are saved in habits.json")
        server.shutdown()


if __name__ == "__main__":
    main()
