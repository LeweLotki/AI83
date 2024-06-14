from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from time import sleep


class GeniusScraper:

    soup = None
    binary_location = '/snap/firefox/current/usr/lib/firefox/firefox'

    def __init__(self): 

        self.web_driver = self.__setup_web_driver() 

    def __del__(self):

        self.web_driver.quit()

    def scrape_url(self, url: str):

        self.web_driver.get(url)
        sleep(1)

        html = self.web_driver.page_source

        self.soup = BeautifulSoup(html, 'html.parser')

        return {
            'url': url,
            'name': self.__get_name(),
            'content': self.__get_content(),
        }

    def get_urls_list(self, url: str):
        self.web_driver.get(url)
        sleep(5)

        last_height = self.web_driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            self.web_driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            sleep(2)
            new_height = self.web_driver.execute_script(
                "return document.body.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height

        html = self.web_driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        
        sized_image_elements = soup.find_all(
            lambda tag: tag.name == 'div' and any(
                cls.startswith('SizedImage') for cls in tag.get('class', [])
            )
        )

        links = []

        for element in sized_image_elements:
            parent_a = element.find_parent('a')
            if parent_a and 'href' in parent_a.attrs:
                links.append(parent_a['href'])

        for link in links:
            print(link)

        return links 

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

    def __get_name(self):
        return

    def __get_content(self):
        return


