# Example code, write your program here
import os
import re
import requests


def get_items():
    url = 'https://frankxfz.me/snapshot.html'
    page = requests.get(url)
    page = page.text

    urls = re.findall(r'href\=\"*(http+.*?)\"*>',page)
    urls_file = open("./output/urls.txt", "w")
    for i in range(len(urls)):
        urls_file.write(urls[i]+'\n')

    bold = re.findall(r'<b>(.*?)</b>',page)
    bold_file = open("./output/bold.txt", "w")
    for i in range(len(bold)):
        bold_file.write(bold[i]+'\n')

    ital = re.findall(r'<i>([\s\S]*?)</i>',page)
    ital_file = open("./output/italics.txt", "w")
    for i in range(len(ital)):
        ital_file.write(ital[i] + '\n')

    red = re.findall(r'\"color:red\">(.*?)</',page)
    red_file = open("./output/red.txt", "w")
    for i in range(len(red)):
        red_file.write(red[i] + '\n')
    return


get_items()