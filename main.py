from scholarly import scholarly, ProxyGenerator
import requests 
from getpass import getpass

API_KEY = "f20fd669a86729dfed87c341d6480197"
pg = ProxyGenerator()
success = pg.ScraperAPI(API_KEY)
print(success)

scholarly.use_proxy(pg)
search_query = scholarly.search_pubs("wbtb induction of lucid dreams")
scholarly.pprint(next(search_query))
# def set_proxy(proxy_type='NoProxy'):
#     if proxy_type.lower() == 'noproxy':
#        print("Using no proxies!")
#        return

#     pg = ProxyGenerator()
#     if proxy_type.lower() == 'scraperapi':
#         proxy_works = pg.ScraperAPI("Yf20fd669a86729dfed87c341d6480197")
#         if proxy_works is True:
#             print("Using ScraperAPI!")
#         elif proxy_works is False:
#             print("ScraperAPI is not working!")
#         elif proxy_works is None:
#             print("Changes have not been reflected")
#         else:
#             print("God knows what is going on", proxy_works)
        
#         scholarly.use_proxy(pg)

# set_proxy('scraperapi')
# author = next(scholarly.search_author())
# scholarly.pprint(author)
# Now search Google Scholar from behind a proxy
# search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
# scholarly.pprint(next(search_query))

# pg = ProxyGenerator()
# success = pg.Tor_Internal(tor_cmd = "C:\\Users\\Home\Desktop\\Tor Browser\\Browser\\firefox.exe")
# scholarly.use_proxy(pg)
# print(requests.get('https://ident.me').text)


