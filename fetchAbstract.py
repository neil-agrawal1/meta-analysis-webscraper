from selenium import webdriver
import pandas as pd
from habanero import Crossref
from pubmed.pubmedsearch import uprint 
from pubmed.pubmedparse import findAbstract
from requests.exceptions import HTTPError 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import re

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
s = Service("C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe")

cr = Crossref()

CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext 

df1 = pd.read_csv("prelimdata.csv")
abstracts = []
print(df1["DOI"])
def fetchAbstract(): 
    for doi in df1['DOI']:
        try: 
            results = cr.works(ids=doi)
            if 'abstract' in results['message']: 
                abstract = cleanhtml(results['message']['abstract'])
                print("Found in Crossref")
                print(doi)
                uprint(abstract)
                abstracts.append(abstract)
            else:
                raise HTTPError
        except HTTPError:
            abstract = findAbstract(doi)
            if abstract == "No Abstract": 
                #sciencedirect
                if "10.1016" in doi: 
                    try: 
                        driver = webdriver.Chrome(service=s, options=options)
                        driver.get("https://doi.org/" + doi)
                        abstractcontainer = driver.find_element("xpath", '//div[@class="abstract author"]')
                        abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                        print("Scidirect paper")
                        print(doi)
                        uprint(abstract)
                        abstracts.append(abstract)
                    except NoSuchElementException:
                        print("Weird Scidirect Article")
                        print(doi)
                        uprint(abstract)
                        abstracts.append("Weird Scidirect " + abstract)
                elif "10.3389" in doi: 
                    try:
                        print("Frontier's Article")
                        driver = webdriver.Chrome(service=s, options=options)
                        driver.get("https://doi.org/" + doi)
                        abstractcontainer = driver.find_element("xpath", "//div[@class=\"JournalAbstract\"]/p")
                        abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                        print(abstract)
                        abstracts.append("Frontier's " + abstract)
                    except NoSuchElementException:
                        print("No Frontier Abstract")
                        print(doi)
                        uprint(abstract)
                        abstracts.append("No Frontier Abstract "  + abstract)
                #IJODR
                elif "10.1158" in doi:
                    driver = webdriver.Chrome(service=s, options=options)
                    driver.get("https://doi.org/" + doi)
                    abstractcontainer = driver.find_element("xpath", '//div[@class="item abstract"]/p')
                    abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                    print(abstract)
                    abstracts.append(abstract)
                #SpringerLink
                elif "10.1007" in doi:
                    try: 
                        driver = webdriver.Chrome(service=s, options=options)
                        driver.get("http://doi.org/" + doi)
                        abstractcontainer = driver.find_element("xpath", '//div[@id="Abs1-content"]/p')
                        abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                        print(abstract)
                        abstracts.append(abstract)    
                    except NoSuchElementException: 
                        abstracts.append("Broken Link")
                        pass
                else: 
                    print ("Not a frontiers article or scidirect")
                    print(doi)
                    abstract = "Not scidirect/frontiers"
                    abstracts.append(abstract)
            else: 
                print("Pubmed Abstract")
                print(doi)
                uprint(abstract)
                abstracts.append(abstract)

fetchAbstract()     
df2 = pd.DataFrame(abstracts, columns=["Abstract"])
print(df2.columns)
papers = pd.concat([df1, df2], axis = 1, ignore_index=True)
print(papers.columns)
papers.to_csv("papers.csv", index=None, header=["DOI", "Title", "Abstract"])
#if you want to remove all the no abstracts from the list, just filter through 
#the papers datafram and remove any row that has "No abstract" in it
#purepapers = papers[~papers["Abstract"].str.contains("No")]["Abstract"]
#print(purepapers)

# page = requests.get("https://www.sciencedirect.com/science/article/abs/pii/S0924933815313729")
# soup = BeautifulSoup(page.content, 'html.parser')
# abstract = soup.find('div', {"id":"preview-section-abstract"})
# uprint(soup.prettify())