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
handle = Entrez.esearch(db="pubmed", term="lucid dreaming induction wbtb", retmax="300", retmode="xml",)
rec_list = Entrez.read(handle)
id_list = rec_list['IdList']

handle = Entrez.efetch(db="pubmed", id=id_list, retmode="xml") #rettype="abstract")
records = handle.read().decode('utf-8')
# uprint(records)

with open ("pubmed/papers.xml", "w", encoding='utf-8') as xml_file: 
    xml_file.write(records)

