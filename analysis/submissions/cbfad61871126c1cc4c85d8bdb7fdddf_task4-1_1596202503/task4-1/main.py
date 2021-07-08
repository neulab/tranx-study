import requests
from bs4 import BeautifulSoup
import os

page = "https://frankxfz.me/snapshot.html"
output_dir = "output"
url_file = os.path.join(output_dir, "urls.txt")
bold_file = os.path.join(output_dir, "bold.txt")
italic_file = os.path.join(output_dir, "italics.txt")
red_file = os.path.join(output_dir, "red.txt")

req = requests.get(page)
soup = BeautifulSoup(req.content, "html.parser")
with open(url_file, "w+") as file_obj:
    for el in soup.find_all('a'):
        eltext = str(el.get('href'))
        if eltext[0:4:] == "http":
            file_obj.write(eltext + "\n")

with open(bold_file, "w+") as file_obj:
    for el in soup.find_all('b'):
        file_obj.write(el.text + "\n")

with open(italic_file, "w+") as file_obj:
    for el in soup.find_all('i'):
        file_obj.write(el.text + "\n")

with open(red_file, "w+") as file_obj:
    for el in soup.find_all('span'):
        if el["style"] == "color:red":
            file_obj.write(el.text + "\n")






