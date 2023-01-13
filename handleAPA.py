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

#"doi = driver.find_element(\"xpath\", '//a[contains(text(), \"doi\")]') \n" ,


def fetchAPAdois(): 
    for link in apapsychurls: 
            f = open("test.py", "w+")
            f.writelines([
            "from selenium import webdriver \n",
            "from selenium.webdriver.common.by import By \n",
            "from selenium.webdriver.chrome.options import Options \n", 
            "options = Options() \n",
            "options.add_argument(\"--headless\") \n",
            "user_agent = \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36\' \n", 
            "options.add_argument(f\'user-agent={user_agent}\') \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "driver = webdriver.Chrome(executable_path=r'C:\\Users\\Home\\seleniumdrive\\chromedriver.exe', options=options) \n",
            f"driver.get('{link}') \n"
            "doi = driver.find_element(By.CSS_SELECTOR, \"span div a\") \n" ,
            "doi = doi.text \n",
            "doi = doi.removeprefix(\"https://doi.org/\") \n",
            "uprint(doi) \n",
            "with open (\"apadois.csv\", \"a\", newline=\"\", encoding=\"utf-8\") as f: \n" ,
                "\tthewriter = csv.writer(f) \n",
                "\tthewriter.writerow([doi])"
                ])
            
            f.close()
            exec(open("test.py").read())
            os.remove("test.py")
    
    apadois = pd.read_csv("apadois.csv", encoding="latin", index_col=False)
    apadois = apadois.drop_duplicates()
    apadois.to_csv("apadois.csv", index=None)

#fetch title and abstract from all apadois.csv and store doi, title, and abstract of APA papers in apadata.csv
def fetchAPAdata(): 
    doisdf = pd.read_csv("apadois.csv")
    dois = doisdf["DOI"].tolist()
    for doi in dois: 
            f = open("test.py", "w+")
            f.writelines([
            "from selenium import webdriver \n",
            "from selenium.webdriver.chrome.options import Options \n", 
            "from selenium.common.exceptions import NoSuchElementException \n",
            "options = Options() \n",
            "options.add_argument(\"--headless\") \n",
            "user_agent = \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36\' \n", 
            "options.add_argument(f\'user-agent={user_agent}\') \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "try: \n"
            "\tdriver = webdriver.Chrome(executable_path=r'C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe', options=options) \n",
            f"\tdriver.get('http://doi.org/{doi}') \n"
            "\ttitle = driver.find_element(By.CSS_SELECTOR, \"h2 a span\") \n", 
            "\tabstract = driver.find_element(By.CLASS_NAME, \"abstract\") \n",
            "\tuprint(title.text) \n"
            "\tuprint(abstract.text) \n",
            "\twith open (\"apadata.csv\", \"a+\", newline=\"\", encoding=\"utf-8\") as f: \n" ,
                "\t\tthewriter = csv.writer(f) \n",
                f"\t\tthewriter.writerow(['{doi}', title.text, abstract.text]) \n"
            "except NoSuchElementException: \n"
            "\t pass" 
                ])
            
            f.close()
            exec(open("test.py").read())
            os.remove("test.py")

    apadata = pd.read_csv("apadata.csv", encoding="latin", index_col=False)
    apadata = apadata.drop_duplicates()
    apadata.to_csv("apadata.csv", index=None)
fetchAPAdois()
fetchAPAdata()
os.remove("test.py")

