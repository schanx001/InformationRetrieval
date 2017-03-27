The archived file contains following source files:
	1. task1.py
		In this file, I have written a code for generating the files which are parsed, tokenized and stored. 
		Note: In my case, some files are not getting generated because the links consist of special codes in them 
		which is why the files are not getting generated. (Approx 930 files are getting generated) 
	2. task2.py
		This file is used to generate n grams and to generate inverted index and term frequency table and document frequency table.
	3.	tf_unigrams.txt
	4.	doc_freq_table_unigrams.txt
	5.	tf_bigrams.txt
	6.	doc_freq_table_bigrams.txt
	7.	tf_trigrams.txt
	8.	doc_freq_table_trigrams.txt
	9.	visitedlist_forTask1HW1.txt  the frontier list from task 1 of hw 1
	10.	readme.txt" 
	11.	stoplist&task3.txt"
	12.	task1-files.txt
	13.	task2-mapper-doc-id-name.txt
	14. three graphs for unigrams,bigrams,trigrams
		
Run the files:
 	In pycharm -> shift+f10
	IDLE -> fn+f5 OR ctrl+f5

Running the assignment in the following order:
	1. 	First run task 1 file task1.py this will create a file "task1-files.txt" which is used in task 2
		for opening the tokenized and parsed files (of links) generated in task1 as an iterator.
	2. 	Run the second file which is task2.py and give input as a value (n=1,2,3 for unigrams bigrams and trigrams) 
		this will generate 3 files for each input given namely an inverted index , term frequency file and 
		document frequency file for given n.
	
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
	
	Lastly:
	
	I have also given nltk package along with the files so that can be used to install nltk without having to download anything.
	Just place that package(nltk-3.2.1) in the Python directory -> Lib -> site-packages 

Citations:
	http://stackoverflow.com/questions/24347029/python-nltk-bigrams-trigrams-fourgrams
	http://www.nltk.org/
	https://piazza.com/class/isqailw8gi021?cid=154 Note: this is for 1000 files not being generated
	https://finnaarupnielsen.wordpress.com/2013/10/22/zipf-plot-for-word-counts-in-brown-corpus/ For zipf's curve 
	