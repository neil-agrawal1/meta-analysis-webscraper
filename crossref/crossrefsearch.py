from habanero import Crossref
import pprint

pp = pprint.PrettyPrinter()

cr = Crossref()
results = cr.works(query="wbtb mild lucid dreaming induction", select="DOI,title", limit=200)


