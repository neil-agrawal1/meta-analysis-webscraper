from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
chrome_options = Options() 
chrome_options.add_argument("--headless") 
import csv 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(executable_path=r'C:\Users\Home\seleniumdrivers\chromedriver.exe') 
driver.get('https://psycnet.apa.org/journals/drm/30/4/287/') 
driver.implicitly_wait(5) 
doi = driver.find_element("xpath", '//a[contains(text(), "doi")]') 
doi = doi.text 
doi = doi.removeprefix("https://doi.org/") 
uprint(doi) 
with open ("apadois.csv", "a", newline="", encoding="utf-8") as f: 
	thewriter = csv.writer(f) 
	thewriter.writerow([doi])