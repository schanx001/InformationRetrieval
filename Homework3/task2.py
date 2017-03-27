import nltk
import operator
import prettytable
from prettytable import PrettyTable
global tf,df,map_doc_id_name,indexfile
tf={}
df=[]
map_doc_id_name={}
doc_freq={}
mapper = open("task2-mapper-doc-id-name.txt", "w+", encoding="utf-8")
#docf=open("doc_freq_table_bigrams.txt","w+",encoding="utf-8")
global filen,termfreqfile,docfreqfile
def main():
    n=input("give the value of n: 1. unigrams 2.bigrams 3.trigrams")
    get_ngrams(n)

def get_ngrams(n):
    global filen,tfobj,docf

    # for Unigrams use this file object

    filen = "inverted_index_unigrams.txt"
    tfobj = "tf_unigrams.txt"
    docf = "doc_freq_table_unigrams.txt"

    #for Bigrams use this objects for file creation

    #filen = "inverted_index_bigrams.txt"
    #tfobj = "tf_bigrams.txt"
    #docf = "doc_freq_table_bigrams.txt"

    #for Trigrams us this objects for file creation

    #filen="inverted_index_trigrams.txt"
    #tfobj="tf_trigrams.txt"
    #docf = "doc_freq_table_trigrams.txt"

    global map_doc_id_name,id_doc,doc_freq,numberoftokens
    numberoftokens={}
    filename = []
    invertedindex_for_ngrams = {}
    f = open("task1-files.txt", "r",encoding="utf-8")
    id_doc=1
    for title in f:
        print(title)
        filename.append(title.rstrip('\n'))

    for docid in filename:

        print(docid+" : "+str(id_doc))
        document_number="A"+str(id_doc)
        map_doc_id_name[id_doc]=[document_number,docid]

        f1 = open(docid + ".txt", "r", encoding="utf-8").read().split()

        # this the number of tokens within each of the documents
        numberoftokens[document_number]=len(f1)
        print("the number of tokens: " + str(numberoftokens[document_number]))

        terms = nltk.ngrams(f1,n)
        count_of_bi_grams = nltk.FreqDist(terms)
        # this loop gives inverted index for specified n for ngrams
        for key,val in count_of_bi_grams.items():
            if key in invertedindex_for_ngrams.keys():
                #if docid not in [x[0] for x in invertedindex_for_bigrams.get(key)]:
                invertedindex_for_ngrams[key].append([document_number,val])
            else:
                invertedindex_for_ngrams[key]=[[document_number,val]]
        id_doc=id_doc+1
    termfreqfile = open(tfobj, "w+", encoding="utf-8")

    # write term frequency table using this loop
    for j in invertedindex_for_ngrams.keys():
        tf[j]=sum([x[1] for x in invertedindex_for_ngrams.get(j)])
    sorted_index = sorted(tf.items(), key=operator.itemgetter(1), reverse=True)
    for i in sorted_index:
        termfreqfile.write(str(i)+"\n")
    termfreqfile.close()
    get_mapped(map_doc_id_name) # write mapping of doc name to doc id


    # write inverted index to file
    indexfile = open(filen, "w+", encoding="utf-8")
    for p in invertedindex_for_ngrams.items():
        indexfile.write(str(p)+"\n")
    indexfile.close()
    stoplist = {}
    # this the loop for writing document frequency table
    for j in invertedindex_for_ngrams.keys():
        docs=[x[0] for x in invertedindex_for_ngrams.get(j)]
        count=len(docs)
        doc_freq[j]=[[docs,count]]

        if count > 475:
            stoplist[j] = count
            print(stoplist[j])

    # stop list code
    sorted_stoplist=sorted(stoplist.items(),key=operator.itemgetter(1),reverse=True)
    stoplistobj = open("stoplist.txt","w+", encoding="utf-8")
    for k in sorted_stoplist:
        stoplistobj.write(str(k) + '\n')
    stoplistobj.close()

    sorted_docf = sorted(doc_freq.items(), key=operator.itemgetter(0), reverse=False)
    docfreqfile = open(docf, "w+", encoding="utf-8")
    # this is for sorted document frequency table lexicographically
    for k in sorted_docf:
        docfreqfile.write(str(k)+"\n")
    docfreqfile.close()

def get_mapped(d):
    sorted_index = sorted(d.items(), key=operator.itemgetter(0), reverse=False)
    for l in sorted_index:
        mapper.write(str(l[1])+"\n")

get_ngrams(1)
# for unigrams give n = 1 and uncomment the file oject while writing for unigrams
# for bigrams give n = 2 similarly for bigrams
# for trigrams give n = 3 similarly for trigrams

