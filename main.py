from scholarly import scholarly, ProxyGenerator
from csv import writer

API_KEY = "f20fd669a86729dfed87c341d6480197"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs("what you want to search on google scholar")

with open('filename.csv', 'w', encoding="utf8", newline='') as f:   
    thewriter = writer(f)
    header = ["Title", "Authors", "Year", "Journal", "Abstract", "DOI"]
    thewriter.writerow(header)

    for i in range(200): 
        publication = next(search_query)
        fullpublication = publication['bib']
        if ("pub_url" in publication):
            fullpublication['DOI'] = publication["pub_url"]
        else: 
            fullpublication['DOI'] = "None"
        thewriter.writerow(list(fullpublication.values()))

