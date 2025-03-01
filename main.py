from src.web.Crawler import Crawler
from src.data.Database import Database

def main():
    starting_page = "https://fortcollinschamber.com/resources/small-business-resources/"
    crawler = Crawler(starting_page)
    # crawler.start()
    with Database("test.db") as db:
        db.create_table("sites", {
            "url": "TEXT UNIQUE"
        })

if __name__ == "__main__":
    main()