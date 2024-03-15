import socketserver
import http.server

class Client:

    def __init__(self, token) -> None:
        self.token = token

    def run(port=8000):
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print()
            httpd.serve_forever()
