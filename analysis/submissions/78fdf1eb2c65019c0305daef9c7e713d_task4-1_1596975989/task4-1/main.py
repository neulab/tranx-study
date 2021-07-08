# Example code, write your program here
import os,re
import requests
def Extractor():
    url = 'https://frankxfz.me/snapshot.html'
    page = requests.get(url)
    page = page.text
    # URLS
    urls = re.findall(r'href\=\"*(http+.*?)\"*>',page)
    urls_file = open("./output/urls.txt", "w")
    for i in range(len(urls)):
        urls_file.write(urls[i]+'\n')
    # BOLD
    bold = re.findall(r'<b>(.*?)</b>', page)
    bold_file = open("./output/bold.txt", "w")
    for i in range(len(bold)):
        bold_file.write(bold[i] + '\n')
    # ITALICS
    ital = re.findall(r'<i>([\s\S]*?)</i>', page)
    ital_file = open("./output/italics.txt", "w")
    for i in range(len(ital)):
        ital_file.write(ital[i] + '\n')
    # RED
    red = re.findall(r'\"color:red\">(.*?)</', page)
    red_file = open("./output/red.txt", "w")
    for i in range(len(red)):
        red_file.write(red[i] + '\n')
    return

if __name__ =='__main__':
    Extractor()