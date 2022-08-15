from Bio import Entrez
import xml.etree.ElementTree as ET
import sys
from csv import writer
import pandas as pd

# from crossref.crossrefparse import apapsychdois

# sys.path.insert(0, 'c:\\Users\\Home\\python-projects\\meta-analysis-webscraper\\crossref')
# print(sys.path)
def uprint(*objects, sep=" ", end="\n", file=sys.stdout):
    enc = file.encoding
    if enc == "UTF-8":
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors="backslashreplace").decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


mytree = ET.parse("pubmed/papers.xml")
root = mytree.getroot()


titles = []
dois = []
apadois = []

for paper in root.findall("./PubmedArticle"):
    # Title
    title = paper.find("MedlineCitation/Article/ArticleTitle").text
    titles.append(title)
    # doi
    doi = paper.find('PubmedData/ArticleIdList/.//ArticleId[@IdType="doi"]')
    if doi is None:
        doi = "No DOI"
        # thewriter.writerow([doi])
    # elif "10.1037" in doi.text:
    #     apapsychdois.append(doi.text)
    elif "10.1037" in doi.text:
        apadois.append("http://doi.org/" + doi.text)

    else:
        dois.append(doi.text)

    def findAbstract():
        abstractWrapper = paper.find("MedlineCitation/Article/Abstract")
        if abstractWrapper is None:
            abstract = "No Abstract"
        else:
            abstract = abstractWrapper.find("AbstractText").text

        return abstract


df = pd.DataFrame(list(zip(dois, titles)), columns=["DOI", "Title"])
apadf = pd.DataFrame(apadois, columns=["DOI"])
df.to_csv("pubmed/pubmeddata.csv", index=None)
apadf.to_csv("apadois.csv", mode="a", index=None, header=None)
