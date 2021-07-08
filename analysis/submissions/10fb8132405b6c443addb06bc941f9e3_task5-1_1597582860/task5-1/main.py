# Example code, write your program here
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver
import requests
import csv
import urllib3

#url = 'localhost:8000/data.csv'

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("localhost", 8000), handler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()




