from bs4 import BeautifulSoup
import urllib.request
import html2text
import time
output = []
l=[]
urllist = []
frontierlist = []
visitedlist = []
all = []
limit = []
getlinks = []

vfile = open('task3.txt', 'w+')


def seedurllist():
    seedurl = 'https://en.wikipedia.org/wiki/Solar_power'
    limit.append(seedurl)

    vfile.write(seedurl + '\n')
    r = urllib.request.urlopen(seedurl).read()
    output = crawl(seedurl)
    soup = BeautifulSoup(r,"lxml")
    for item in output:
        frontierlist.append(item)
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

limit=['https://en.wikipedia.org/wiki/Solar_power']
def visited(list, depth):
    count = 0
    visit = list
    for i in visit:
            time.sleep(1)
            getlinks = crawl(i)
            link = crawl(i)
            list.extend(getlinks)
            for j in link:
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
