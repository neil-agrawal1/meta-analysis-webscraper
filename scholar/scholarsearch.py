from scholarly import scholarly, ProxyGenerator

API_KEY = "44b8adae25f0c547d268f699c158d170"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs("wbtb mild lucid dreaming")
# add user input feature for searching google scholar


