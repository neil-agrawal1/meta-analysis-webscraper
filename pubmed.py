from Bio import Entrez
import sys
import xml.etree.ElementTree as ET

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


Entrez.email="lenter360@gmail.com"
handle = Entrez.esearch(db="pubmed", term="lucid dreaming", retmax="200", retmode="xml",)
rec_list = Entrez.read(handle)
id_list = rec_list['IdList']

handle = Entrez.efetch(db="pubmed", id=id_list, retmode="xml") #rettype="abstract")
records = handle.read().decode('utf-8')
# uprint(records)

with open ("information.xml", "w", encoding='utf-8') as xml_file: 
    xml_file.write(records)

mytree = ET.parse('information.xml')
root = mytree.getroot()
# uprint(myroot[0][0][2][4][0].text)

counter = 1
for elm in root.findall("./PubmedArticle/MedlineCitation/Article"): 
    uprint(f"Title {counter}: " + elm.find('ArticleTitle').text)
    abstractWrapper = elm.find('Abstract')
    if abstractWrapper is None: 
        abstract = "No Abstract" 
    else: 
        abstract = abstractWrapper.find('AbstractText').text

    if abstract is None: 
        abstract = "No Abstract"
        
    uprint("Abstract: " + abstract)
    doi = elm.find("ELocationID")
    if doi is None: 
        doi = "No DOI"
    else: 
        doi = doi.text
    uprint("DOI: http://doi.org/" + doi + "\n")
    counter = counter + 1