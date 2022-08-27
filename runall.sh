set -e 

#crossref
python crossref/crossrefsearch.py #searches the databse and brings back query results
python crossref/crossrefparse.py #parses query results, creates crossrefdata.csv which contains titles and dois 

#pubmed
python pubmed/pubmedsearch.py #searches the database and brings back query results   
python pubmed/pubmedparse.py #parses query, creates pubmeddata.csv with titles and dois

#google scholar
python scholar/scholarsearch.py #searches google scholar database and brings back query results
python scholar/scholarparse.py #parses query results, creates scholar.csv which contains titles, urls, and other information
python scholar/fetch-dois.py #pulls dois manually from all the urls, creates scholardata.csv with titles and dois

python combine-prelimdata.py #combines titles and dois from all 3 databses
python handleAPA.py #does two things, one pull dois from specifically the APA links and two 
                    #searches for all the abstracts. Stores doi, title, and abstracts in apadata.csv

python fetchAbstract.py #fetches abstract from all data collected and creates prelimdata.csv with titles, dois, and abstracts
python combine-alldata.py #combines apadata.csv and prelimdata.csv into papers.csv

