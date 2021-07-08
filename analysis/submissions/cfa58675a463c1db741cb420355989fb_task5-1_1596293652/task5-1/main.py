# Example code, write your program here

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pandas as pd
from urllib.parse import urlparse, parse_qs
import re

df = pd.read_csv('data.csv')
regex = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
class S(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        p = urlparse(self.path)
        q = parse_qs(p.query)
        email = q['email'][0]
        if not regex.search(email):
            self.send_response(400)
            self.send_header('Connection', 'close')
            self.end_headers()
            return
        ip = q['ip'][0]
        d = df[(email == df['email']) & (ip == df['ip_address'])]
        if len(d):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(bytes(json.dumps({
                'first_name': d.iloc[0]['first_name'],
                'last_name': d.iloc[0]['last_name'],
                'gender': d.iloc[0]['gender'],
            }), encoding='utf-8'))
            return
        else:
            self.send_response(404)
            self.send_header('Connection', 'close')
            self.end_headers()
            return



m = HTTPServer(('127.0.0.1', 8000), S)

try:
    m.serve_forever()
except KeyboardInterrupt:
    pass

m.server_close()

