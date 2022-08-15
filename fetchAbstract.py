from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from habanero import Crossref
from pubmed.pubmedsearch import uprint 
from pubmed.pubmedparse import findAbstract
from requests.exceptions import HTTPError 
from selenium.common.exceptions import NoSuchElementException
import re
import requests 
from bs4 import BeautifulSoup

# result = driver.find_element("xpath", '//div/p')
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--disable-browser-side-navigation')

cr = Crossref()
# uprint(cr.works(ids="http://doi.org/10.26355/eurrev_202104_25559"))
# result = cr.works(ids="https://doi.org/10.1093/sleep/zsab294")
# abstract = result['message']['abstract']

CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext 

df = pd.read_csv("prelimdata.csv")
abstracts = []
def fetchAbstract(): 
    for doi in df['DOI']:
        try: 
            results = cr.works(ids=doi)
            title = results['message']['title']
            uprint(title)
            if 'abstract' in results['message']: 
                abstract = results['message']['abstract']
                uprint(cleanhtml(abstract))
                abstracts.append(abstract)
            else:
                raise HTTPError
        except HTTPError:
            abstract = findAbstract()
            if abstract == "No Abstract": 
                #sciencedirect
                if "10.1016" in doi: 
                    try: 
                        driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
                        driver.get("https://doi.org/" + doi)
                        abstractcontainer = driver.find_element("xpath", '//div[@class="abstract author"]')
                        abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                        abstracts.append(abstract)
                        print("Found scidirect abstract")
                        print(doi)
                    except NoSuchElementException:
                        abstract = "No Abstract"
                        abstracts.append(abstract)
                        print("Can't find abstract in SciDirect")
                        print(doi)
                else: 
                    abstract = "No abstract"
                    print("Not a Scidirect Abstract, look elsewhere")
                    print(doi)
            else: 
                abstracts.append(abstract) 
                print("added pubmed abstract")      
    
    print(abstracts)

fetchAbstract()     
# uprint(abstracts)
#     # //tag[contains(text(), ’text’)]

# page = requests.get("https://www.sciencedirect.com/science/article/abs/pii/S0924933815313729")
# soup = BeautifulSoup(page.content, 'html.parser')
# abstract = soup.find('div', {"id":"preview-section-abstract"})
# uprint(soup.prettify())