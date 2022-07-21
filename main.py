from scholarly import scholarly, ProxyGenerator
from csv import writer

API_KEY = "f20fd669a86729dfed87c341d6480197"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

hello = "meme"

search_query = scholarly.search_pubs("wbtb lucid dreaming induction")

with open('wbtbpapers.csv', 'w', encoding="utf8", newline='') as f:   
    thewriter = writer(f)
    header = ["Title", "Authors", "Year", "Journal", "Abstract", "DOI"]
    thewriter.writerow(header)

    for i in range(20): 
        publication = next(search_query)
        # print(type(list(publication['bib'].values())))
        fullpublication = publication['bib']
        fullpublication['DOI'] = publication["pub_url"]
        thewriter.writerow(list(fullpublication.values()))


    


# publication = next(search_query)
# publication2 = next(search_query)
# print(publication['bib'])
# print(publication2['bib'])

# information = publication['bib']
# Title = information['title']
# Abstract = information['abstract']
# Author = information['author']
# Year = information['pub_year']

# info = [Title, Abstract, Author, Year]
# print(info) 