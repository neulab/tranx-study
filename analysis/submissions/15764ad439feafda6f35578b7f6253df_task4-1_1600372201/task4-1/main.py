# Example code, write your program here
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re
import colorama
import os
url = 'https://frankxfz.me/snapshot.html'
html_page = requests.get(url).text
soup = BeautifulSoup(html_page, "html.parser")
f = open("output/urls.txt", "w")
f1 = open("output/italics.txt", "w")
f2 = open("output/bold.txt", "w")
f3 = open("output/red.txt", "w")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    f.writelines(link.get('href'))
    f.write("\n")
results1 = soup.find('span', style=lambda x: x and 'red' in x)
for i in soup.findAll('i'):
    f1.writelines(i.text)
    f1.write("\n")
for i in soup.findAll('b'):
    f2.writelines(i.text)
    f2.write("\n")
for i in soup.findAll('span', style=lambda x: x and 'red' in x):
    f3.writelines(i.text)
    f3.write("\n")

