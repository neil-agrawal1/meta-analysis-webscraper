from scholarly import scholarly, ProxyGenerator

API_KEY = "f20fd669a86729dfed87c341d6480197"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs("wbtb lucid dreaming induction")
 
for i in range(20): 
    publication = next(search_query)
    print(publication['bib'])
    


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