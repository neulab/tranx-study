from bs4 import BeautifulSoup
import requests

url = "https://frankxfz.me/snapshot.html"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
links = []
for a in soup.find_all('a', href=True):
    link = a['href']
    if 'https' in link:
        links.append(link)

bolds = []
for strong_tag in soup.find_all('b'):
    bolds.append(strong_tag.text)

italics = []
for ita in soup.find_all('i'):
    italics.append(ita.text)

red = []
for col in soup.find_all('span'):
    red.append(col.text)

with open('output/urls.txt', 'w') as out:
    out.write('\n'.join(links))

with open('output/italics.txt', 'w') as out:
    out.write('\n'.join(italics))

with open('output/bold.txt', 'w') as out:
    out.write('\n'.join(bolds))

with open('output/red.txt', 'w') as out:
    out.write('\n'.join(red))



