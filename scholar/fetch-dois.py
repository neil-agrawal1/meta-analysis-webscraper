from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
prefs = {
    "download.open_pdf_in_system_reader": False,
    "download.prompt_for_download": False,
    "download.default_directory": "/dev/null",
    "plugins.always_open_pdf_externally": False}
options.add_experimental_option(
    "prefs", prefs
)
s = Service("C:\\Users\\Home\\seleniumdrivers\\chromedriver.exe")

df = pd.read_csv("scholar/scholar.csv")
urls = df[~df["Link"].str.contains("apa.org" and "None")]["Link"].tolist()
 
scholarinfo = pd.read_csv("scholar/scholar.csv", index_col=False)
dois = []
titles = []

def fetchDOIfromURL():
    for url in urls:
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(url)

        try:
            doi = driver.find_element("xpath", '//a[contains(text(), "doi")]')
            doi = doi.text.removeprefix("https://doi.org/")
            dois.append(doi)
            title = scholarinfo.loc[scholarinfo["Link"] == url]
            title.reset_index(drop=True, inplace=True)
            title = title["Title"][0]
            titles.append(title)
            print(doi)
            print(title)
            driver.set_page_load_timeout(5)
        except NoSuchElementException:
            continue
    driver.quit()

    scholardata = pd.DataFrame(list(zip(dois, titles)), columns=["DOI", "Title"])
    scholardata.to_csv("scholar/scholardata.csv", index=None)

fetchDOIfromURL()