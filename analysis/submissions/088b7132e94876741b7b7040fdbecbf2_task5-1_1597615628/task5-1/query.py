import requests
import csv
import json
from urllib.parse import  urlencode

DICT = {}
DATA = {'email':'mmackettrick0@latimes.com','ip_address':'233.43.85.181'}
quer=urlencode(DATA)
req=requests.get('http://localhost:8000/data.csv',params = DATA)
fd = open('file.csv','w')
fd.write(req.text)
fd.close()
counter = 0
with open('file.csv',newline="") as fp:
    reader = csv.reader(fp,delimiter= ',')
    for i in reader:
        if DATA['email'] == i[3] and DATA['ip_address'] == i[5]:
            counter+=1
            DICT['first_name'] = i[1]
            DICT['last_name'] = i[2]
            DICT['gender'] = i[4]
            print(str(req.status_code)+"OK")

if counter==0:
    print("404"+"Not Found")
else :
    print(json.dumps(DICT))