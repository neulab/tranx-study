# Example code, write your program here
import re
import requests
import csv
import json
#from urllib.parse import urlencode

my_dict = {}
data = {'email':'mmackettrick0@latimes.com', 'ip_address':'233.43.85.181'}
#qq = urlencode(data)
req = requests.get('http://localhost:8000/data.csv', params=data)
#print(req.text)

f1 = open('output.csv', 'w')
f1.write(req.text)
f1.close()
counter = 0
with open ('output.csv', newline="") as f2:
    reader = csv.reader(f2, delimiter=',')
    for i in reader:
        if data['email'] == i[3] and data['ip_address'] == i[5]:
            counter += 1
            my_dict['first_name'] = i[1]
            my_dict['last_name'] = i[2]
            my_dict['gender'] = i[4]
            print(str(req.status_code) + " OK")


if counter == 0:
    print("404" + " Not Found")
else:
    print(json.dumps(my_dict))
