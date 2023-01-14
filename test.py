from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
options = Options() 
options.add_argument("--headless") 
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36' 
options.add_argument(f'user-agent={user_agent}') 
import csv 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(executable_path=r'C:\Users\Home\seleniumdrive\chromedriver.exe', options=options) 
driver.get('https://psycnet.apa.org/journals/drm/30/4/287/') 
doi = driver.find_element(By.CSS_SELECTOR, "span div a") 
doi = doi.text 
doi = doi.removeprefix("https://doi.org/") 
uprint(doi) 
with open ("datafiles/apadois.csv", "a", newline="", encoding="utf-8") as f: 
	thewriter = csv.writer(f) 
	thewriter.writerow([doi])