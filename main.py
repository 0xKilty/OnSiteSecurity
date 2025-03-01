from src.Crawler import Crawler

def main():
    starting_page = "https://fortcollinschamber.com/resources/small-business-resources/"
    crawler = Crawler(starting_page)
    crawler.start()

if __name__ == "__main__":
    main()