# Example code, write your program here
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#os.makedirs("output/images")
my_path = '/vagrant/task4-2/output/images'
img_box = []
imgs = soup.find_all('div', class_='thumb')
pd.read_html(requests.get(URL).content, header='csv')[-1].to_csv("output/populations.csv")
for img in imgs:
    img_url = img.attrs.get("src")
    urllib.request.urlretrieve(img_url, my_path + os.path.basename(img))
    print(img_url)

