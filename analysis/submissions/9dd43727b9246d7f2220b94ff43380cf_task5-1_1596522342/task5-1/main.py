from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import csv
import re

csv_file = open ('data.csv', 'r')
csvList= csv.reader(csv_file)



class requestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.path = '/query'
        self.send_response(200)
        self.end_headers()
        output1 = '<html><body><h1> Enter the email and ip address </h1></body></html>'
        self.wfile.write(bytes(output1, 'utf-8'))
        output2 = '<html><body>'
        output2 += '<form method="POST" enctype="multipart/form-data" action="/query/response">'
        output2 += '<input name="email" type="text" placeholder="Enter email">'
        output2 += '<br>'
        output2 += '<input name="ip" type="text" placeholder="Enter ip address">'
        output2 += '<br>'
        output2 += '<input type="Submit" value="Submit">'
        output2 += '</form></body></html>'
        self.wfile.write(bytes(output2, 'utf-8'))

    def do_POST(self):
        global csvList
        ctype, ddict = cgi.parse_header(self.headers.get('content-type'))
        ddict['boundary'] = bytes(ddict['boundary'], 'utf-8')
        fields = cgi.parse_multipart(self.rfile, ddict)
        email = fields.get('email')
        ip = fields.get('ip')
        email = email[0].decode()
        entryFound = 0
        EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if not EMAIL_REGEX.match(email):
            self.send_response(400)
            entryFound = -2
            print ("ERROR EMAIL")
            IP_REGEX = re.compile(r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$''')
            if not IP_REGEX.match(email):
                self.send_response(400)
                entryFound = -2
                print ("ERROR IP")

        x = 0
        ip = ip[0].decode()
        if entryFound == 0:
            entryFound = -1
        for x in csvList:
            if x[3] == email and x[5] == ip:
                entryFound = x
                break
        if entryFound == -2:
            output = "Invalid email or IP \n\n\n"
            self.send_response(400)

        elif entryFound == -1:
            self.send_response(404)
            output = "ERROR 404.. Entry not found\n\n\n"
        else:
            self.send_response(200)
            output = ''
            output += '{\n\t"firstname":"'
            output += x[1]
            output +='",\n\t"lastname":"'
            output += x[2]
            output += '",\n\t"Gender":"' + x[4] + '"\n}\n\n'
            print (output)
            self.send_response(301)

        self.wfile.write(bytes(output, 'utf-8'))
        self.end_headers()





server = HTTPServer(('localhost',8000), requestHandler)
server.serve_forever()

