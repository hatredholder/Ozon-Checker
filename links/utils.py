import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent


def get_info(url):
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.opera}")
    options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    service = Service("D:\Старый диск 1\Programming\Python\Selenium\chromedriver\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "lxml")
        name = soup.find(attrs={"data-widget":"webProductHeading"}).next_element.text.strip()
        price = int("".join([i for i in soup.find(attrs={"slot":"content"}).next_element.next_sibling.next_element.next_element.next_element.text if i.isnumeric()]))
        return name, price

    except Exception:
        pass
    finally:
        driver.close()
        driver.quit()
