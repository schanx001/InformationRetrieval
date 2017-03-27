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
vfile = open('visitedlist_forTask1.txt', 'w+')


def seedurllist():
    f = open("wikicrawler.txt", 'wb')
    lfile = open("links.txt", 'w+')
    seedurl = 'https://en.wikipedia.org/wiki/Sustainable_energy'
    limit.append(seedurl)

    vfile.write(seedurl + '\n')
    r = urllib.request.urlopen(seedurl).read()
    output = crawl(seedurl)
    soup = BeautifulSoup(r,"lxml")
    f.write(soup.renderContents(prettyPrint=str))
    f.close()
    for item in output:
        frontierlist.append(item)
        lfile.write("{0}{1}\n".format('https://en.wikipedia.org', item))
    lfile.close()
    visited(frontierlist,1)

def crawl(f):
    data = urllib.request.urlopen(f).read()
    soup = BeautifulSoup(data, "lxml")
    for link in soup.find_all('a'):
        txt = str(link.get('href'))
        if txt.startswith('/wiki'):
            if ':' in txt:
                continue
            else:
                if '#' in txt:
                    txt = txt.partition("#")[0].rstrip()
                if link.get('href') not in urllist:
                    print(l)
                    urllist.append(txt)
                    l.append('https://en.wikipedia.org'+txt)
    return l

limit=['https://en.wikipedia.org/wiki/Sustainable_energy']
def visited(list, depth):
    count = 0
    visit = list
    for i in visit:
            getlinks = crawl(i)
            time.sleep(1)
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
    exit()
    vfile.close()

seedurllist()
