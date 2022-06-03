import time

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_info(url):
    """Get info from URL using Selenium"""
    useragent = UserAgent()

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.opera}")
    options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

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
