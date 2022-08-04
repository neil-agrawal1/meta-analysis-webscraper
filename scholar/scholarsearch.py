from scholarly import scholarly, ProxyGenerator

API_KEY = "f20fd669a86729dfed87c341d6480197"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs("wbtb induction lucid dreaming")
# add user input feature for searching google scholar


