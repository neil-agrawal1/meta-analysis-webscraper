from selenium import webdriver
import pandas as pd
from habanero import Crossref
from pubmed.pubmedsearch import uprint 
from pubmed.pubmedparse import findAbstract
from requests.exceptions import HTTPError 
from selenium.common.exceptions import NoSuchElementException
import re

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--disable-browser-side-navigation')

cr = Crossref()

CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext 

df1 = pd.read_csv("prelimdata.csv")
abstracts = []
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
                        driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
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
                    print("Frontier's Article")
                    print(abstract)
                    abstracts.append("Frontier's " + abstract)
                #IJODR
                elif "10.1158" in doi:
                    driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
                    driver.get(doi)
                    abstractcontainer = driver.find_element("xpath", '//div[@class="item abstract"]/p')
                    abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                    print(abstract)
                    abstracts.append(abstract)
                #SpringerLink
                elif "10.1007" in doi:
                    driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
                    driver.get(doi)
                    abstractcontainer = driver.find_element("xpath", '//div[@id="Abs1-content"]/p')
                    abstract = cleanhtml(abstractcontainer.get_attribute("innerHTML"))
                    print(abstract)
                    abstracts.append(abstract)    
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

# fetchAbstract()     

# df2 = pd.DataFrame(abstracts, columns=["Abstract"])
# print(df2)
# papers = pd.concat([df1, df2], axis = 1)
# papers.to_csv("papers.csv")
#     # //tag[contains(text(), ’text’)]

# page = requests.get("https://www.sciencedirect.com/science/article/abs/pii/S0924933815313729")
# soup = BeautifulSoup(page.content, 'html.parser')
# abstract = soup.find('div', {"id":"preview-section-abstract"})
# uprint(soup.prettify())