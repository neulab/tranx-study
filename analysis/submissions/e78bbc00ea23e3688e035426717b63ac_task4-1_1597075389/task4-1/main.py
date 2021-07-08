import requests
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import os.path

data_folder = os.path.join("output")

r = requests.get('https://frankxfz.me/snapshot.html')
soup = BeautifulSoup(r.text)
http = httplib2.Http()
status, response = http.request('https://frankxfz.me/snapshot.html')

#Look for urls and write to file
file_to_open = os.path.join(data_folder, "urls.txt")
with open(file_to_open, 'w') as fw:
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            site = link['href'].split()
            if site[0][0] == 'h' and site[0][1] == 't' and site[0][2] == 't':
                fw.write(site[0] + '\n')

#Look for bold and write to file
file_to_open = os.path.join(data_folder, "bold.txt")
with open(file_to_open, 'w') as fw:
    for tag in ['b', 'h2', 'h3', 'h4']:
        for heading in soup.find_all(tag):
            fw.write(heading.text + '\n')

#Look for italics and write to file
file_to_open = os.path.join(data_folder, "italics.txt")
with open(file_to_open, 'w') as fw:
    for heading in soup.find_all('i'):
        fw.write(heading.text + '\n')

#Look for red and write to file
file_to_open = os.path.join(data_folder, "red.txt")
with open(file_to_open, 'w') as fw:
    for heading in soup.find_all('span'):
        fw.write(heading.text + '\n')


