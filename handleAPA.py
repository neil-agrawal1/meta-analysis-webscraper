import os, csv, sys
import pandas as pd

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

#pull doi from APA.org articles
apapsychurls=[]
df = pd.read_csv("scholar/scholar.csv")
apapsychurls = df[df['Link'].str.contains("apa.org")]['Link'].tolist()

def fetchAPAdois(): 
    for link in apapsychurls: 
            f = open("test.py", "w+")
            f.writelines([
            "from selenium import webdriver \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe') \n",
            f"driver.get('{link}') \n"
            "driver.implicitly_wait(1) \n",
            "doi = driver.find_element(\"xpath\", '//a[contains(text(), \"doi\")]') \n" ,
            "uprint(doi.text) \n",
            "with open (\"apadois.csv\", \"a\", newline=\"\", encoding=\"utf-8\") as f: \n" ,
                "\tthewriter = csv.writer(f) \n",
                "\tthewriter.writerow([doi.text])"
                ])
            
            f.close()
            exec(open("test.py").read())
            os.remove("test.py")

# fetchAPAdois()

#fetch title and abstract and store in a file with doi, title, and abstract
def fetchAPAdata(): 
    doisdf = pd.read_csv("apadois.csv")
    dois = doisdf["DOI"].tolist() 
    for doi in dois: 
            f = open("test.py", "w+")
            f.writelines([
            "from selenium import webdriver \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe') \n",
            f"driver.get('{doi}') \n"
            "driver.implicitly_wait(1) \n",
            "title = driver.find_element(By.CSS_SELECTOR, \"h2 a span\") \n", 
            "abstract = driver.find_element(By.CLASS_NAME, \"abstract\") \n",
            "uprint(title.text) \n"
            "uprint(abstract.text) \n",
            "with open (\"apadata.csv\", \"a+\", newline=\"\", encoding=\"utf-8\") as f: \n" ,
                "\tthewriter = csv.writer(f) \n",
                f"\tthewriter.writerow(['{doi}',title.text, abstract.text])"
                ])
            
            f.close()
            exec(open("test.py").read())
            os.remove("test.py")

fetchAPAdata()
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
# driver.get("https://psycnet.apa.org/doiLanding?doi=10.1037%2Fa0020881")
# title = driver.find_element(By.CSS_SELECTOR, "h2 a span") 
# print(title.text)title = driver.find_element(By.CSS_SELECTOR, "h1 span") 
