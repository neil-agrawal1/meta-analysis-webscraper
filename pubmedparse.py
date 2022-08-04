from Bio import Entrez
import xml.etree.ElementTree as ET
import sys 
from csv import writer

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

mytree = ET.parse('information.xml')
root = mytree.getroot()

with open ("pubmeddois.csv", "w", encoding="UTF-8", newline='') as file: 
    thewriter = writer(file)
    header = ["DOI"]
    thewriter.writerow(header)

    for paper in root.findall("./PubmedArticle/MedlineCitation/Article"): 
        #Title
        title = paper.find('ArticleTitle').text 
        #Abstract
        # abstractWrapper = paper.find('Abstract')
        # if abstractWrapper is None: 
        #     abstract = "No Abstract" 
        # else: 
        #     abstract = abstractWrapper.find('AbstractText').text

        # if abstract is None: 
        #     abstract = "No Abstract"  

    #DOI
    for paper in root.findall("./PubmedArticle/PubmedData/ArticleIdList"): 
        doi = paper.find('.//ArticleId[@IdType="doi"]')
        if doi is None:
            doi = "No DOI"
            print("No DOI")
        else: 
            doi = doi.text
            thewriter.writerow(["http://doi.org/" + doi])


    # uprint(f"Title {counter}: " + title)
    # # uprint("Abstract: " + abstract)