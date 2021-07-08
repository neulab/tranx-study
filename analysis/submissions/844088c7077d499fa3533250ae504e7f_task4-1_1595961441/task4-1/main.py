import requests
from bs4 import BeautifulSoup
import validators

html = requests.get('https://frankxfz.me/snapshot.html')
bs = BeautifulSoup(html.text, features='html.parser')

with open('output/urls.txt', 'w') as f:
    for aElem in bs.find_all('a'):
        if 'href' in aElem.attrs and validators.url(aElem['href']):
            f.write('{}\n'.format(aElem['href']))

with open('output/bold.txt', 'w') as f:
    for boldElem in bs.find_all('b'):
        f.write('{}\n'.format(boldElem.text))

with open('output/italics.txt', 'w') as f:
    for itElem in bs.find_all('i'):
        f.write('{}\n'.format(itElem.text))

with open('output/red.txt', 'w') as f:
    for redElem in bs.find_all(attrs={'style': 'color:red'}):
        f.write('{}\n'.format(redElem.text))
