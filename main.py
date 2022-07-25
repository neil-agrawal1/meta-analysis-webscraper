from scholarly import scholarly, ProxyGenerator
from csv import writer

API_KEY = "Your Key"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs("what you want to search on google scholar")

with open('filename.csv', 'w', encoding="utf8", newline='') as f:   
    thewriter = writer(f)
    header = ["Title", "Authors", "Year", "Journal", "Abstract", "Link"]
    thewriter.writerow(header)

    for i in range(200): 
        publication = next(search_query)
        fullpublication = publication['bib']
        if ("pub_url" in publication):
            fullpublication['Link'] = publication["pub_url"]
        else: 
            fullpublication['Link'] = "None"
        thewriter.writerow(list(fullpublication.values()))

