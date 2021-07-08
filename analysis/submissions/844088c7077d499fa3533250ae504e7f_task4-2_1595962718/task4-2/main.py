from bs4 import BeautifulSoup
import csv
import os
import requests

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
bs = BeautifulSoup(requests.get(url).text, features='html.parser')

if not os.path.exists('output/images'):
    os.makedirs('output/images')

with open('output/populations.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['country', 'population'])

    table_body = bs.find('tbody')
    for row in table_body.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) < 2:
            continue # Skip the first row
        country_name = [elem for elem in cols[0].find_all('a') if len(elem.text) > 0][0].text
        if country_name.strip() == '':
            print(row)
            break
        writer.writerow([country_name, int(cols[1].text.replace(',', ''))])
        img_url = 'https:' + cols[0].find('img')['src']
        with open('output/images/{}.png'.format(country_name), 'wb') as img_f:
            img_f.write(requests.get(img_url).content)
