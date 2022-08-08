from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import csv
import sys

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service('C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe')

driver = webdriver.Chrome(service = s, options=options)

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
testurls2 = ["https://psycnet.apa.org/journals/drm/30/4/287/", "https://psycnet.apa.org/journals/drm/30/4/287/"]
driver.get("https://psycnet.apa.org/journals/drm/30/4/287/")
driver.implicitly_wait(1)
doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
print(doi.text)
sys.exit()

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
    
# testurls = ["https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full","https://psycnet.apa.org/journals/drm/30/4/287/", "https://www.sciencedirect.com/science/article/pii/S0149763418303361", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full", "https://psycnet.apa.org/record/2020-24631-001", "https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01383/full" ]
with open ("scholar/scholardois.csv", "w", encoding="utf-8", newline="") as file: 
    thewriter = csv.writer(file)
    header = ["DOI"]
    thewriter.writerow(header)
    counter = 0

    for url in urls: 
        driver.get(url)
        driver.implicitly_wait(1)
        
        try: 
            doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
            thewriter.writerow([doi.text])
            print(doi.text)
        except NoSuchElementException: 
            counter = counter + 1
            continue         

print(counter)

