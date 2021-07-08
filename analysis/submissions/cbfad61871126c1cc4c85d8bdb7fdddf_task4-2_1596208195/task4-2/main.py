import requests
from bs4 import BeautifulSoup
import csv
import os
import re

page = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
req = requests.get(page)
soup = BeautifulSoup(req.content, "html.parser")
image_dir = os.path.join("output", "images")
csv_file = os.path.join("output", "population.csv")
data = []

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

table = soup.find("tbody")
for row in table.find_all("tr"):
    i = 0
    country = ""
    population = ""
    for cell in row.find_all("td"):
        if i == 0:
            country = cell.find("a").text
            flag = "http:" + cell.find("img")["src"]
            flag_req = requests.get(flag)
        elif i == 1:
            population = cell.text.replace(",", "")
        if country and population:
            data.append({"country":country, "population":population})
            flag_filename = country + ".png"
            with open(os.path.join(image_dir, flag_filename), "wb") as file_img:
                file_img.write(flag_req.content)
            break
        i += 1
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["country", "population"])
    writer.writeheader()
    for line in data:
        writer.writerow(line)