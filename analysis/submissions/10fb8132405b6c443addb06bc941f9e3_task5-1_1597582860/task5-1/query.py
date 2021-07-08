import requests
import csv
import json
from urllib.parse import urlencode

mydict={}
data = {'email':'mmackettrick0@latimes.com','ip_address': '233.43.85.181'}
qq = urlencode(data)
r = requests.get('http://localhost:8000/data.csv', params=data)
f = open('file.csv','w')
f.write(r.text)
f.close()
count=0
with open('file.csv', newline="") as f1:
    reader = csv.reader(f1, delimiter=',')
    for i in reader:
        if data['email'] == i[3] and data['ip_address'] == i[5]:
            count += 1
            mydict['first_name']=i[1]
            mydict['last_name'] = i[2]
            mydict['gender'] = i[4]
            print(str(r.status_code) + "  OK")
        #elif not (re.search(r'\w+@\w+.\w+',data['email'])).group():
         #   print("400" + "  Bad Request")

if count==0:
    print("404" + "  Not Found")
else:
    print(json.dumps(mydict))
