# Example code, write your program here
import os,re,requests,shutil
import urllib.request

def World():
    url ='https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    page = requests.get(url)
    page = page.text
    page = re.findall(r'<th>Country([\S\s]*?)</tbody></table>',page)
    page = page[0]
    # Population
    temp = re.findall(r'<td.*>([\d,]*)</td>',page)
    pop = []
    for i in range(len(temp)):
        if temp[i]:
            pop = pop + [temp[i].replace(',','')]
    # Country
    temp = re.findall(r'\">([a-zA-Z\s\(\)\-éíãçÅ\"\,\.><\/]*)?</a>[^\)]', page)
    coun = []
    for i in range(len(temp)):
        if temp[i]:
            coun = coun + [temp[i].split("<")[0]]
    # Flag
    temp = re.findall(r'src=\"//(.*?)\"', page)
    flag = []
    for i in range(len(temp)):
        if temp[i]:
            flag = flag + [temp[i]]
    # Output file
    out = open('./output/populations.csv',"w")
    out.write('country,population\n')
    for i in range(len(coun)):
        out.write(coun[i] + ',' + pop[i] + '\n')
    print(coun)

    # Download images
    if os.path.isdir('./output/images/'):
        None
    else:
        os.mkdir('./output/images/')
    for i in range(len(coun)):
        r = requests.get('http://' + flag[i], stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open('./output/images/'+coun[i]+".jpg", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    return

if __name__ == '__main__':
    World()