import os, csv, sys
import pandas as pd


apapsychurls=[]
df = pd.read_csv("scholar/scholar.csv")
apapsychurls = df[df['Link'].str.contains("apa.org")]['Link'].tolist()
print(apapsychurls)


for link in apapsychurls: 
        f = open("test.py", "w+")
        f.writelines([
        "from selenium import webdriver \n",
        "import csv \n",
        "from selenium.webdriver.common.by import By \n"
        "driver = webdriver.Chrome(executable_path=r'C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe') \n",
        f"driver.get('{link}') \n"
        "driver.implicitly_wait(1) \n",
        "doi = driver.find_element(\"xpath\", '//a[contains(text(), \"doi\")]') \n" ,
        "abstract = driver.find_element(By.CLASS_NAME, \"abstract\") \n",
        "uprint(doi.text) \n",
        "uprint(abstract.text) \n",
        "with open (\"scholar/apainformation.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f: \n" ,
            "\tthewriter = csv.writer(f) \n",
            "\tthewriter.writerow([\"DOI\", \"Abstract\"]) \n",
            "\tthewriter.writerow([doi.text, abstract.text])"
            ])
        
        f.close()
        exec(open("test.py").read())
        os.remove("test.py")