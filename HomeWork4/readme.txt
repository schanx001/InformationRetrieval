Readme file for homework4 :
This archive contains follwoing files:

	1. task2RetrievalModule.py
		I have integrated the Homework3 parser/tokenizer and indexing module into the Homework4. To run the HW3 code (for parsing/indexing)
		uncomment the hw3() in the code and uncomment the parser/tokenizer function and indexer function as well. By default it will run HW4 main() on 
		the inverted index I am submitting with this archive. It takes around 10-15 mins to run HW3 code for generating the tokenized files and indexing 
		runs in about 15-20 seconds. HW4 runs in about 1-2 minutes for all the 4 queries given. Queries I am reading from a file as mentioned in the Homework document.
	
	2. top_100_task2_Query1.txt
	3. top_100_task2_Query2.txt
	4. top_100_task2_Query3.txt
	5. top_100_task2_Query4.txt
	6. Lucene_Q1_top100.txt
	7. Lucene_Q2_top100.txt
	8. Lucene_Q3_top100.txt
	9. Lucene_Q4_top100.txt
	
	10. HW4.java 
			This is the file given by Professor for Lucene Search Engine.
			Run this file on any java IDE (Netbeans) add the libraries given for lucene.
			Change the query id for each query (I have mentioned this in the code as comments). It generates a file for each query.
	
	11. Brief_discussion_of_2_search_engines.txt // HW4
	
	12. Report_of_implementation.txt // HW4
	
	13.	readme.txt 
	
	14. query_file.txt // consists of 4 queries 
	
	15. task2-mapper-doc-id-name.txt
	
 	16. visitedlist_forTask1HW1.txt // used in HW3
	
	17. inverted_index_unigrams.txt // inverted index used in HW4
	
	18. task1-files.txt  // Used in Parser , Tokenizer and Indexer functions of HW3
	
	19. tokenscount.txt      // Number of terms in each document
	
Run the files:
 	In pycharm -> shift+f10
	IDLE -> fn+f5 OR ctrl+f5

Running the assignment :
		1. Firstly directly you can run the main() for the query retrieval.
		2. If the parsing and indexing code is to be run then uncomment the hw3 function and comment out main() so that one task runs at a time.
		3. The hw3 function calls the parsing and indexer function so, first uncomment the parser function call in the hw3 function so that it can generate tokenized files
			after which the indexer function is called and it generates the inverted index for unigrams.
		4. If the hw3 code is not to be run then directly the HW4 main() can be called which uses already created inverted index and some auxiliary files.
		
Set up and Installations:
	Note: this library is important for task2 to run so please install this first.

	Installing library NLTK :
		Install NLTK: http://pypi.python.org/pypi/nltk
	
	OR
	
	Command Line for python :
	
		>>>	import nltk
		>>> nltk.download('all')
	
	OR
	
		In PyCharm goto file -> settings -> project interpreter -> +(green plus sign) -> search nltk -> install nltk
	
Citations:
	For Homework3:
	
	http://stackoverflow.com/questions/24347029/python-nltk-bigrams-trigrams-fourgrams
	http://www.nltk.org/
	https://piazza.com/class/isqailw8gi021?cid=154 Note: this is for 1000 files not being generated
	
	For Homework4:
	
	http://www.lucenetutorial.com/advanced-topics/scoring.html
	https://stanford.edu/~rjweiss/public_html/IRiSS2013/text2/notebooks/tfidf.html
	https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/
	http://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html