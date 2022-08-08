from habanero import Crossref
from csv import writer
from crossrefsearch import results


doi_list = results['message']['items'] 
apapsychdois = []

with open ("crossref/crossrefdois.csv", "w", encoding="UTF-8", newline="") as file: 
    thewriter = writer(file)
    header = ["DOI"]
    thewriter.writerow(header)

    for i in doi_list: 
        thewriter.writerow(["http://doi.org/" + i['DOI']])
       
            
