#!/bin/bash


python crossref/crossrefsearch.py; python crossref/crossrefparse.py & 
python pubmed/pubmedsearch.py;python pubmed/pubmedparse.py &
python scholar/scholarsearch.py; python scholar/scholarparse.py; python scholar/fetch-dois.py 

python combine-prelimdata.py ; python handleAPA.py & python fetchAbstract.py ; python combine-alldata.py 
