from selenium import webdriver 
import csv 
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(executable_path=r'C:\Users\neila\seleniumdrivers\chromedriver.exe') 
driver.get('https://doi.org/10.1037/h0094362') 
driver.implicitly_wait(5) 
title = driver.find_element(By.CSS_SELECTOR, "h2 a span") 
abstract = driver.find_element(By.CLASS_NAME, "abstract") 
uprint(title.text) 
uprint(abstract.text) 
with open ("apadata.csv", "a+", newline="", encoding="utf-8") as f: 
	thewriter = csv.writer(f) 
	thewriter.writerow(['https://doi.org/10.1037/h0094362', title.text, abstract.text])