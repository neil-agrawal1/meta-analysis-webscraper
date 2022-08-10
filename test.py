from selenium import webdriver 
import csv 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(executable_path=r'C:\Users\Home\seleniumdrivers\chromedriver.exe') 
driver.get('https://psycnet.apa.org/journals/drm/30/4/287/') 
driver.implicitly_wait(1) 
doi = driver.find_element("xpath", '//a[contains(text(), "doi")]') 
abstract = driver.find_element(By.CLASS_NAME, "abstract") 
uprint(doi.text) 
uprint(abstract.text) 
with open ("scholar/scholarseleniuminfo.csv", "a", newline="", encoding="utf-8") as f: 
	thewriter = csv.writer(f) 
	thewriter.writerow(["DOI", "Abstract"]) 
	thewriter.writerow([doi.text, abstract.text])