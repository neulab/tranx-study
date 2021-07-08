# Example code, write your program here
from bs4 import BeautifulSoup
import requests
import os
import re

url="https://frankxfz.me/snapshot.html"
target_folder = 'output'

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")
#print(soup.prettify()) # print the parsed data of html

# for link in soup.find_all('a', href=re.compile(r'^[(http)(https)]://')):
#     print(link)

for link in soup.select('a[href^="https"]'):
    with open(os.path.join(target_folder, "urls.txt"), 'a+') as filehandler:
        filehandler.writelines(link.get('href') + '\n')
filehandler.close()

for link in soup.findAll('b'):
    with open(os.path.join(target_folder, "bold.txt"), 'a+') as filehandler:
        filehandler.writelines(link.string + '\n')

for link in soup.findAll('i'):
    with open(os.path.join(target_folder,"italic.txt"), 'a+') as filehandler:
        filehandler.writelines(link.string+'\n')

for link in soup.findAll('span', {"style":"color:red"}):
    if link.attrs['style'] == "color:red":

        with open(os.path.join(target_folder,"red.txt"), 'a+') as filehandler:
            filehandler.writelines(link.string+'\n')