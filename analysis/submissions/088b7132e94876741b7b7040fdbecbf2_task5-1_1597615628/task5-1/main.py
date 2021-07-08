from http.server import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler
import http.server
import socketserver
import csv
import urllib3
import sys
import requests
HandlerClass = SimpleHTTPRequestHandler
ServerClass = HTTPServer
Protcol = "HTTP/1.1"
if sys.argv[1:]:
    port = int(sys.argv[1])
else :
    port = 8000
server_address = ('127.0.0.1',port)
HandlerClass.protocol_version = Protcol
httpd = ServerClass(server_address,HandlerClass)

sa =  httpd.socket.getsockname()
print("Trying localhost..." ,sa[0],"TCP_NODELAY set",sa[1],"Connected to localhost port 8000 (#0)","...")
httpd.serve_forever()