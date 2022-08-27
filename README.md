# meta-analysis-webscraper
This repository scrapes data from 3 databases: CrossRef, Google Scholar, and PubMed. 
The main data that is scraped are titles, DOIs, and abstracts of papers. 

To run the program, use a bash terminal and type bash runall.sh. 
## Set Up
To scrape google scholar, you will need a [scraperAPI](https://www.scraperapi.com/) key. Just use the free trial, you will have enough free credits to run the program. 
You don't need scraperAPI to scrape CrossRef or PubMed

You will also need a VPN to run the program successfully. 
(Check if program needs VPN to run pubmed and cross ref data) 

## Scripts

CrossRef
* `crossref/crossrefsearch.py` - searches the database and brings back query results
* `crossref/crossrefparse.py` - parses query results, creates crossrefdata.csv which contains titles and DOIs 

PubMed
* `pubmed/pubmedsearch.py`- searches the database and brings back query results   
* `pubmed/pubmedparse.py`- parses query, creates pubmeddata.csv with titles and DOIs

Google Scholar
* `scholar/scholarsearch.py`- searches google scholar database and brings back query results
* `scholar/scholarparse.py`- parses query results, creates scholar.csv which contains titles, urls, and other information
* `scholar/fetch-dois.py`- pulls dois manually from all the urls, creates scholardata.csv with titles and DOIs

Others
* `combine-prelimdata.py`- Combines csvs containing titles and DOIs from all 3 databases
* `handleAPA.py`- Pulls DOIs from specifically the APA links collected from Google Scholar. It then searches for abstracts for all APA papers. Stores the DOIs, titles, and abstracts in apadata.csv
* `fetchAbstract.py` - Fetches abstract from all data collected and creates prelimdata.csv with titles, DOIs, and abstracts
* `combine-alldata.py` - Combines apadata.csv and prelimdata.csv into papers.csv

 
```

