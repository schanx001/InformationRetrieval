from bs4 import BeautifulSoup
import urllib.request
import html2text
import time
import json
import re

output = list()
l=list()
urllist = list()
frontierlist = list()
visitedlist = list()
all = list()
limit = list()
getlinks = list()
vfile = open('BFS_focused.txt', 'w+')


def seedurllist(keyword):
    seedurl = 'https://en.wikipedia.org/wiki/Sustainable_energy'
    limit.append(seedurl)

    vfile.write(seedurl + '\n')
    r = urllib.request.urlopen(seedurl).read()
    output = crawl(seedurl,keyword)
    soup = BeautifulSoup(r,"lxml")
    for item in output:
        frontierlist.append(item)

    visited(frontierlist,keyword)

def crawl(f,keyword):
    data = urllib.request.urlopen(f).read()
    soup = BeautifulSoup(data, "lxml")
    for link in soup.find_all('a'):
        txt = str(link.get('href'))
        anchortxt = link.text
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
                        if link.get('href') not in urllist:
                            urllist.append(txt)
                            l.append('https://en.wikipedia.org'+txt)
    return l

limit=['https://en.wikipedia.org/wiki/Sustainable_energy']
def visited(list,keyword):
    count = 0
    visit = list
    depth = 2
    for i in list:
        if depth <=5:
            getlinks = crawl(i,keyword)
            time.sleep(1)
            for i in getlinks:

                link = crawl(i,keyword)

                list.extend(getlinks)
                for j in list:

                    if len(limit) <= 1000:
                            if j not in limit:
                                limit.append(j)
                                vfile.write(j+"\n")

                            else:
                                continue
                    else:
                            exit()
                depth=depth+1

    print(depth)

    exit()
    vfile.close()

seedurllist('solar')
