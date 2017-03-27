from bs4 import BeautifulSoup
import urllib.request
import re
import nltk
import html2text
import time
global lst
lst = []
def main():
    global rx,lst,w
    #soup = BeautifulSoup(r, "lxml")
    f = open("visitedlist_forTask1HW1.txt", 'r',encoding="utf-8")
    x = f.readlines()
    # filename for opening the documents in task2
    new= open("task1-files.txt","w+",encoding="utf-8")
    for k in x:
        temp = urllib.request.urlopen(k).read()
        soup = BeautifulSoup(temp, "lxml")
        for title in soup.find_all('h1'):
            t = str(title.text).title().replace(" ","")
            t=re.sub('\)\(\-','',t).strip()
            if t not in lst:
                lst.append(t)
            print(t)
            w = open(t + ".txt", "w+",encoding='utf-8')
            w.write(title.text.lower() + '\n')
        for link in soup.find_all(['p']):
            #print(link.text)
            rx=re.compile('\[\d+\]|\(|\)|\{|\}|,|[""]|/|;|:').sub(' ',link.text).strip()
            rx=re.sub(r'(?<!\d)\.|\.(?!\d)',"",rx)
            rx = re.sub(r'(?<!\d)\,|\,(?!\d)', "", rx)
            rx = rx.lower()
            rx = rx.split()
            for j in rx:
                if j!='-':
                    w.write(str(j) + '\n')

    for k in lst:
        new.write(k+"\n")
    new.close()
    w.close()
    f.close()
    #print(soup.get_text)
main()
