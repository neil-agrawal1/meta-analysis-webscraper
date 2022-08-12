from csv import writer
from scholarsearch import search_query

with open('scholar/scholar.csv', 'w', encoding="utf8", newline='') as f:   
    thewriter = writer(f)
    header = ["Title", "Authors", "Year", "Journal", "Abstract", "Link"]
    thewriter.writerow(header)

    scholarurls = []
    for i in range(30): 
        publication = next(search_query)
        fullpublication = publication['bib']
        if ("pub_url" in publication):
            fullpublication['Link'] = publication["pub_url"]
            scholarurls.append(publication['pub_url'])
        else: 
            fullpublication['Link'] = "None"
        thewriter.writerow(list(fullpublication.values()))

