from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv 

driver = webdriver.Chrome(executable_path = r"C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe")

urls = []
with open ("scholar/scholar.csv", "r", encoding="utf-8-sig") as f: 
    reader = csv.reader(f)
    # DictReader
    for row in reader: 
        if (row[5] == "None"):
            continue
        else:  
            urls.append(row[5])

    del urls[0]


testurls = ["https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full","https://psycnet.apa.org/journals/drm/30/4/287/", "https://www.sciencedirect.com/science/article/pii/S0149763418303361", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full", "https://psycnet.apa.org/record/2020-24631-001", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full" ]

for url in testurls: 
    driver.get(url)
    driver.implicitly_wait(3)
    
    try: 
        doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
        print(doi.text)
    except NoSuchElementException: 
        print("No DOI")
        continue         

    sleep(2)

driver.quit()