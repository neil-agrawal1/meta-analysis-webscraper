from habanero import Crossref
import pprint

pp = pprint.PrettyPrinter()

cr = Crossref()
results = cr.works(query="wbtb lucid dreaming", select="DOI", limit=200)
# pp.pprint(results)

