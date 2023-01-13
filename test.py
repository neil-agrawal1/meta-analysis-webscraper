from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException 
options = Options() 
options.add_argument("--headless") 
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36' 
options.add_argument(f'user-agent={user_agent}') 
import csv 
from selenium.webdriver.common.by import By 
try: 
	driver = webdriver.Chrome(executable_path=r'C:\Users\Home\seleniumdrivers\chromedriver.exe', options=options) 
	driver.get('http://doi.org/10.1037/drm0000114') 
	driver.implicitly_wait(5) 
	title = driver.find_element(By.CSS_SELECTOR, "h2 a span") 
	abstract = driver.find_element(By.CLASS_NAME, "abstract") 
	uprint(title.text) 
	uprint(abstract.text) 
	with open ("apadata.csv", "a+", newline="", encoding="utf-8") as f: 
		thewriter = csv.writer(f) 
		thewriter.writerow(['10.1037/drm0000114', title.text, abstract.text]) 
except NoSuchElementException: 
	 pass