import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from .scraper import GeniusScraper

from models.songs import TableSongs


class Scraper:
    '''This class is called by CLI command to initialize scraper service'''    
    
    genius_url = 'https://genius.com/'

    def __init__(self):  
        '''Initializing particular scrapers constructors'''

        logging.basicConfig(filename='scraper.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.genius_scraper = GeniusScraper()

    def scrape_url(self, url: str | None = None):
        '''
        This is main method of class, it works as follow:
            -> scrape all urls from given url and save them to db
            -> iterate through urls in db and scrape all significant data from them
            -> save collected data to db and change flag scraped if scraped succesfully
        '''

        urls_to_scrape = [self.genius_url] 
        for url in urls_to_scrape:

            try:
                data = self.__collect_genius_data(url=url)
                if data:
                    is_data_complete = self.__commit_collected_data(data)
                    if is_data_complete:
                        self.logger.info(f'Succesfully scraped: {url}')
                    db.session.commit()

            except Exception as e:
                self.logger.error(f"Error scraping {url}: {e}")
                db.session.rollback()

    def __collect_genius_data(self, url: str) -> dict:
        '''This method collect data scraped from given url from db'''

        genius_data = self.genius_scraper.scrape_url(url=url)

        return genius_data 

    def __commit_collected_data(self, data: dict) -> bool:
        '''
        This method commits collected data to db if not defective.
        Return True if data complete, return False if data defective.
        '''

        required_fields = [
            'url', 
            'name', 
            'content',
        ]

        if all(data.get(field) is not None for field in required_fields):

            new_song = TableSongs(
                url=data['url'],
                name=data['name'],
                content=data['content'],
            )
            db.session.add(new_song)
            
            return True

        else: 
            return False


