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
            "from selenium.webdriver.chrome.options import Options \n", 
            "chrome_options = Options() \n",
            "chrome_options.add_argument(\"--headless\") \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe') \n",
            f"driver.get('{link}') \n"
            "driver.implicitly_wait(5) \n",
            "doi = driver.find_element(\"xpath\", '//a[contains(text(), \"doi\")]') \n" ,
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

#fetch title and abstract and store in a file with doi, title, and abstract
def fetchAPAdata(): 
    doisdf = pd.read_csv("apadois.csv")
    dois = doisdf["DOI"].tolist()
    for doi in dois: 
            f = open("test.py", "w+")
            f.writelines([
            "from selenium import webdriver \n",
            "from selenium.webdriver.chrome.options import Options \n", 
            "from selenium.common.exceptions import NoSuchElementException \n",
            "import csv \n",
            "from selenium.webdriver.common.by import By \n"
            "try: \n"
            "\tdriver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe') \n",
            f"\tdriver.get('http://doi.org/{doi}') \n"
            "\tdriver.implicitly_wait(5) \n",
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

fetchAPAdois()
fetchAPAdata()
# apadata = pd.read_csv("apadata.csv")
# apadata = apadata.drop_duplicates()
# apadata.to_csv("apadata.csv", index=None)
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path=r'C:\\Users\\neila\\seleniumdrivers\\chromedriver.exe')
# driver.get("https://psycnet.apa.org/doiLanding?doi=10.1037%2Fh0094324")
# driver.implicitly_wait(5)
# title = driver.find_element(By.CSS_SELECTOR, "h2 a span") 
# # abstract = driver.find_element(By.CLASS_NAME, "abstract") 
# print(title.text)
# print(abstract.text)
# title = driver.find_element(By.CSS_SELECTOR, "h1 span") 

#headless options
# "chrome_options = Options() \n",
# "chrome_options.add_argument('--lang=en_US') \n", 
# "chrome_options.add_argument(\"--no-sandbox\") \n"
# "chrome_options.add_argument(\"--headless\") \n",
# "chrome_options.add_argument('--disable-gpu') \n", 
# "chrome_options.add_argument(\"--disable-extensions\") \n",             
# "chrome_options.add_argument(\"--window-size=1920,1080\") \n",
# "chrome_options.add_argument(\"start-maximized\") \n",
# "chrome_options.add_experimental_option(\"excludeSwitches\", [\"enable-automation\"]) \n",
# "chrome_options.add_experimental_option(\"useAutomationExtension\", False) \n",
# "chrome_options.add_argument(\"--proxy-server='direct://'\"); \n",
# "chrome_options.add_argument(\"--proxy-bypass-list=*\"); \n",