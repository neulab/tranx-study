# Example code, write your program here
#https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
import requests
from bs4 import BeautifulSoup
import re
import urllib
import pprint
import os
import urllib.parse
from os.path  import basename

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
x = requests.get(url)
soup = BeautifulSoup(x.content, 'html.parser')

output={}
table = soup.table
table = soup.find('table')
table_rows = table.find_all('tr')
upload_link= []
folder = 'output/images'

for tr in table_rows:
    td = tr.find_all('td')
    image_link = [i.img for i in td]
    if image_link != []:
        #print(image_link[0])
        src = re.findall(r'src="\/\/.{0,160}\.png', str(image_link))
        src_srt = src[0]
        src_srt = 'https:' + src_srt[5:]
        #print(src_srt)

    row = [i.text for i in td]
    if row != []:
        output[re.sub(r'\[.+\]', '', row[0][1:])] = row[1]
        #print(row[0])
        #urllib.request.urlretrieve(os.path.join(folder, output[0]), "mp3.mp3")
        response = requests.get(src_srt)
        if response.status_code == 200:
            with open(os.path.join(folder, row[0]+'.png'), 'wb') as f:
                f.write(response.content)
import csv
csv_columns = ['country','population']
dict_data = output
csv_file = "output/populations.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for key in output.keys():
            csvfile.write("%s,%s\n" % (key, output[key]))
except IOError:
    print("I/O error")
