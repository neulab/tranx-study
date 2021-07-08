import requests
import os.path
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

r = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(r.text)
table = soup.find('table',{'class':'wikitable sortable'})
data_folder = os.path.join("output")

#Create sequences for gathering correct values
s1 = []
for num in range(0,1000):
    val = 1 + num*5
    s1.append(val)
s2 = []
for num in range(0,1000):
    val = 2 + num*5
    s2.append(val)

#country list required to create image names later
countries = []

#Find the countries and populations and store them in the csv file
file_to_open = os.path.join(data_folder, "populations.csv")
with open(file_to_open, 'w') as f:
    f.write('country,population\n')
    i = 1
    for rows in table.find_all('td'):
        #Sequences used here to only catch the rows of text required
        if i in s1:
            string = rows.text
            country = ''
            n = 0
            for char in string:
                #If loop is used to filter out anything in brackets and leading whitespace
                if char in '[(':
                    break
                elif n == 0:
                    n = 1
                    continue
                else:
                    country = country + char
            #This is just for the Cocos Islands to stop islands getting cut off
            if i == 1196:
                country = country + 'Islands'

        elif i in s2:
            string = rows.text
            pop = ''
            #Remove commas
            for char in string:
                if char == ',':
                    continue
                else:
                    pop = pop + char
            f.write(country + ',' + pop + '\n')
            countries.append(country)
        i += 1

data_folder = os.path.join("output/images")
#Store the page urls for images
urls = []
images = table.find_all('img')
for image in images:
    url = 'https:' + image['src']
    urls.append(url)

i = 0
#Copy images to images folder
for country in countries:
    file_to_open = os.path.join(data_folder, country + '.png')
    with open(file_to_open, 'wb') as f:
        uopen = urllib.request.urlopen(urls[i])
        stream = uopen.read()
        f.write(stream)
    i += 1