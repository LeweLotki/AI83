from models import init_db
from scraper import Scraper

def main():
    init_db()
    print("Database initialized!")
    scraper = Scraper()
    scraper.scrape_url()

if __name__ == "__main__":
    main()

