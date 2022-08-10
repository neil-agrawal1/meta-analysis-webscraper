from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from habanero import Crossref
from pubmed.pubmedsearch import uprint 
from pubmed.pubmedparse import findAbstract
from requests.exceptions import HTTPError 
import re
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

df = pd.read_csv("dois.csv")
    
for doi in df['DOI']:
    try: 
        results = cr.works(ids=doi)
        title = results['message']['title']
        uprint(title)
        if 'abstract' in results['message']: 
            abstract = results['message']['abstract']
            uprint(cleanhtml(abstract))
    except HTTPError:
        findAbstract()
    
    if "10.1037" in doi: 
        driver = webdriver.Chrome(executable_path=r'C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe', chrome_options=ChromeOptions)
        driver.get(doi)
        abstract = driver.find_element(By.CLASS_NAME, "abstract")
        print(abstract.text)
        continue 
    
    
#     # //tag[contains(text(), ’text’)]

