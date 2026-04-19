import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            body = b"OK - Bot is running."
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    print(f"Health-check server on port {PORT}")
    server.serve_forever()

def run_in_background():
    t = threading.Thread(target=start_web_server, daemon=True)
    t.start()
