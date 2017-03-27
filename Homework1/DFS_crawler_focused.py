from bs4 import BeautifulSoup
import urllib.request
import html2text
import re
import time
temp=[]
ret = []
keyword='solar'

def cr(url,keyword):
    ret=[]
    temp=[]
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, "lxml")
    for link in soup.find_all('a'):
            txt = str(link.get('href'))
            anchortxt= link.text
            if txt.startswith('/wiki'):
                if ':' in txt:
                    continue
                else:
                    if '#' in txt:
                        txt = txt.partition("#")[0].rstrip()
                    if keyword in txt or keyword.capitalize() in txt or keyword.upper() in txt \
                            or keyword.lower() in txt or keyword in anchortxt \
                            or keyword.lower() in anchortxt or keyword.upper() in anchortxt \
                            or keyword.capitalize() in anchortxt:
                            if txt not in temp:
                                temp.append(txt)
                                ret.append('https://en.wikipedia.org'+txt)

    return ret

visited =list()
f=open('fi1.txt','w+')
f.write('https://en.wikipedia.org/wiki/Sustainable_energy'+'\n')
visited=['https://en.wikipedia.org/wiki/Sustainable_energy']

def dfs(url,depthlimit):
    if depthlimit<=5:
        front=cr(url,keyword)
        for item in front:
                if len(visited) <= 1000:
                    if item not in visited:
                            f.write(item+'\n')
                            visited.append(item)
                            print(depthlimit)
                            dfs(item,depthlimit+1)
                    else:
                        continue
                else:
                    exit()


dfs('https://en.wikipedia.org/wiki/Sustainable_energy',1)
f.close()