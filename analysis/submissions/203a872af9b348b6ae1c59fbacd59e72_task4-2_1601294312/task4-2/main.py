import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

table = soup.find_all("table")[0]

data = []
for rows in table.find_all('tr')[1:]:
    try:
        sub_row = rows.find_all('td')
        name = sub_row[0].find('a').contents[0]
        pop = sub_row[1].text.replace(",", "")
        data.append([name, pop])
        try:
            image_link = str(sub_row[0]).split('src="//')[1].split('"')[0]
            img = requests.get("https://" + image_link)
            with open('output/images/' + name + '.png', 'wb') as out:
                out.write(img.content)
        except:
            continue
    except:
        continue

with open('output/populations.csv', 'w') as out:
    out.write('country, population\n')
    for d in data:
        try:
            out.write(','.join(d) + '\n')
        except:
            continue
