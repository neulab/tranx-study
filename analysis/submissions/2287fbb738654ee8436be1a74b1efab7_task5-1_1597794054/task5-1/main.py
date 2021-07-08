# Example code, write your program here

from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver

# http.server.HTTPServer("127.0.0.1")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", 8000), handler) as httpd:
    print("serving at port ", 8000)
    httpd.serve_forever()
