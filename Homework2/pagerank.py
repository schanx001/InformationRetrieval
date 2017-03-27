from math import log
import operator
import itertools
global inlinks,outlinks,pr,p,s,totalpages,newpr,hpr,sinkpr,perplexity,outl,sinkl
inlinks = {}
outlinks={}
pr={}
p=[]
s=[]
newpr={}
totalpages=0
d=0.85
hpr=0
sinkpr=0
perplexity=0
outl = {}
sinkl = {}
count_inlinks=0
# perp=open('perplexity_task2_G2.txt','w+') # for graph G2
# t50=open('top50_G2.txt','w+') # for graph G2

perp=open('perplexity_task2_G1.txt','w+')
t50=open('top50_G1.txt','w+')

def getpages(filename):
    global count_inlinks
    f=open(filename,'r')
    for docid in f.readlines():
        # split the words by space because the document is formatted likewise
        items = docid.split()

        #create a key,value pair as given in the document
        # take first word as the key and the rest as values
        inlinks[items[0]] = items[1:]
        # get all the pages as keys in p
        p.append(items[0])
	# no of inlinks of each page
    for links in inlinks.keys():
        if len(inlinks.get(links)) == 0:
            count_inlinks=count_inlinks+1
    print("the number links with no inlinks :" + str(count_inlinks))

    global outl,sinkl
    # get outlinks count for each page
    outl = getoutlinks(inlinks)
    # get all sink nodes from the corpus
    sinkl = getsinknodes(inlinks)
    print(len(p))
    #print(sinkl)
    print("sink nodes number:")
    print(len(sinkl))
    # send pages to pagerank calculator
    calculatePageRank(p)

def getoutlinks(inlinks):
    # get values of each page
    for page in inlinks.keys():
        for v in inlinks.get(page):
            # for every value increment their outlinks counter
            if v in outlinks:
                outlinks[v]+= 1
            else:
                # first time set the outlink count to 1
                outlinks[v] = 1
    return outlinks

def getsinknodes(inlinks):
    for i in inlinks.keys():
        # get those pages which are not present in the outlinks
        # i.e they dont have any outlinks
        if i not in outlinks.keys():
            s.append(i)
    return s

def calculatePageRank(pages):
    global outl,sinkl,perplexity,inlinks

    for page in pages:
        pr[page]=float(1)/float(len(pages))     # calculate initial page rank for each page

    count=0
    #print(len(pages))
    while count<4: # run while for 4 iterations (where change in perplexity is less than 1 back to back)
        sinkpr=0
        for pagep in sinkl:
            sinkpr+=pr[pagep] #calculate total sink PageRank
        #print(sinkpr)
        for pagep in pages:

            newpr[pagep] = (1-d)/float(len(pages)) #teleportation
            newpr[pagep]+=d*sinkpr/float(len(pages)) #spread remaining sink pagerank evenly

            for pageq in inlinks[pagep]: # pages pointing to page p

                newpr[pagep]+=(d*pr.get(pageq))/outl.get(pageq) # add share of pagerank from inlinks
        for pagep in pages:
            pr[pagep]=newpr[pagep]
        backtrack = perplexity # keep track of previous perplexity
        perplexity = calculate_perplexity(pr) # new perplexity
        #print(perplexity)
        perp.write(str(perplexity)+"\n")
        if (abs(perplexity-backtrack))<1:  # calculate difference between previous and current perplexity
            count=count+1 # increment if difference is less than 1
        else:
            count
        #print(backtrack)
        #print(perplexity)
    perp.close()
    top_50_links(pr) # get top 50 links

    top_5_by_inlinks(inlinks) # get top 5 pages by inlinks (based on their count)

def calculate_perplexity(pr):
    global hpr
    hpr=0
    for page in pr.keys():
        hpr+=pr[page]*log(1/pr[page],2) # calculate entropy and add for each page
    return 2**hpr # return perplexity

def top_50_links(pr):
    # get items for the pr dictionary , use key to get the values (i.e itemgetter(1))
    # Get the descending order with reverse = True
    sorted_pr = sorted(pr.items(), key=operator.itemgetter(1),reverse=True)
    print("top 50 by page rank are:\n")
    for j in sorted_pr[0:50]: # get top 50 results
        t50.write(str(j)+"\n")
    t50.close()
    print(sorted_pr[0:50])

def top_5_by_inlinks(inlinks):
    list_of_inlinks={}
    sorted_inlinks={}
    # get count of inlinks for each page
    for p in inlinks.keys():
        list_of_inlinks[p]=len(inlinks.get(p))
    # get a sorted list
    sorted_inlinks=sorted(list_of_inlinks.items(),key=operator.itemgetter(1),reverse=True)
    print("top 5 by inlinks are:\n")
    top_5=sorted_inlinks[0:5] # get top 5 results
    print(top_5)

# give the filenames to calculate pagerank in the following way:

#getpages('wt2g_inlinks.txt')  # graph given as G2

getpages('graph_from_task1A.txt') # graph created from task 1 as G1

