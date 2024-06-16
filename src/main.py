from models import init_db
from scraper import Scraper
from chat_gpt import Prompter

def main():
    init_db()

    scraper = Scraper()
    scraper.scrape_url()

    Prompter()

if __name__ == "__main__":
    main()

