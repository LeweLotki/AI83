from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from time import sleep

class SudokupadScraper:

    soup = None
    binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'

    def __init__(self): 

        self.web_driver = self.__setup_web_driver() 

    def __del__(self):

        self.web_driver.quit()

    def scrape_url(self, url):

        self.web_driver.get(url)
        sleep(1)

        html = self.web_driver.page_source

        self.soup = BeautifulSoup(html, 'html.parser')
        
        return {
        }

    def __setup_web_driver(self):

        options = Options()
        options.add_argument("--headless")
        options.binary_location = self.binary_location
        options.profile = webdriver.FirefoxProfile()

        gecko_driver_manager = GeckoDriverManager()
        gecko_driver = gecko_driver_manager.install()

        service = FirefoxService(gecko_driver)

        web_driver = webdriver.Firefox(
            service=service,
            options=options
            )

        return web_driver


