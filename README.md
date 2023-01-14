# meta-analysis-webscraper
The purpose of the "meta-analysis-webscraper" is to accelerate the creation of meta-analyses in research. Specifically, this code speeds up the process of finding relevant papers that can be utilized in a meta-analysis. 

Type in key words related to the topic you are researching. This repository scrapes data from 3 main databases: CrossRef, Google Scholar, PubMed, and APA PsycNet. The main data that is scraped are titles, DOIs, and abstracts of papers. 

Once a csv file with relevant papers is generated, run the project through [ASReview Lab](https://asreview.nl/), an active learning software that screens large amounts of text, to generate the most useful papers. 

To run the program, use a bash terminal and type `bash runall.sh`. 
## Set Up
To scrape google scholar, you will need a [scraperAPI](https://www.scraperapi.com/) key. Just use the free trial, you will have enough free credits to run the program. 
You don't need scraperAPI to scrape CrossRef or PubMed

You will also need a VPN to run the program successfully. 

## Scripts

CrossRef
* `crossref/crossrefsearch.py` - searches the crossref database and brings back query results
* `crossref/crossrefparse.py` - parses query results, creates crossrefdata.csv which contains titles and DOIs 

PubMed
* `pubmed/pubmedsearch.py`- searches the pubmed database and brings back query results   
* `pubmed/pubmedparse.py`- parses query, creates pubmeddata.csv with titles and DOIs

Google Scholar
* `scholar/scholarsearch.py`- searches google scholar and brings back query results
* `scholar/scholarparse.py`- parses query results, creates scholar.csv which contains titles, urls, and other information
* `scholar/fetch-dois.py`- pulls any dois that can be found from the urls. A new file "scholardata.csv" is created with just titles and DOIS.

Others
* `combine-prelimdata.py`- Combines CSV files containing titles and DOIs from all 3 databases
* `handleAPA.py`- Pulls DOIs from specifically the APA links collected from Google Scholar. It then searches for abstracts for specifically all APA papers. Stores the DOIs, titles, and abstracts in apadata.csv
* `fetchAbstract.py` - Fetches abstract from all papers (not APA) collected and creates prelimdata.csv with titles, DOIs, and abstracts
* `combine-alldata.py` - Combines apadata.csv and prelimdata.csv into papers.csv

 
```

