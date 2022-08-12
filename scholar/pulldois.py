from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import csv
import os, sys
import pandas as pd

from bs4 import BeautifulSoup
from lxml import etree
import requests

# sys.path.insert(1, r'C:\\Users\\Home\\python-projects\\meta-analysis-webscraper\\pubmed')
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--headless')
options.add_argument('--disable-gpu')
s = Service('C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe')

# stealth(driver,
#       languages=["en-US", "en"],
#       vendor="Google Inc.",
#       platform="Win32",
#       webgl_vendor="Intel Inc.",
#       renderer="Intel Iris OpenGL Engine",
#       fix_hairline=True,
#   )


# testurls = ["https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full","https://psycnet.apa.org/journals/drm/30/4/287/", "https://www.sciencedirect.com/science/article/pii/S0149763418303361", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full", "https://psycnet.apa.org/record/2020-24631-001", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full" ]
#return DOIs from rest of scholar links
df = pd.read_csv("scholar/scholar.csv")
urls = df[~df['Link'].str.contains("apa.org")]['Link'].tolist()

scholarinfo = pd.read_csv("scholar/scholar.csv", index_col = False)
print(scholarinfo)
dois = []
titles = []
scholardata = pd.DataFrame(list(zip(dois,titles)), columns=["DOI", "title"])

for url in urls: 
    driver = webdriver.Chrome(service = s, options=options)
    driver.get(url)

    try: 
        doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
        dois.append(doi.text)
        title = scholarinfo.loc[scholarinfo['Link'] == url]['Title']
        title = title.to_string()
        titles.append(title)
        print(dois)
        print(titles)
    except NoSuchElementException: 
        continue         

  
#Handle Apa.org


#code to write only apa dois to own text file 
# "with open (\"apadois.txt\", \"a\", encoding=\"utf-8\") as f: \n" ,
#             "\tf.write(doi.text + \"\\n\")"])
