from src.web.Crawler import Crawler
from src.data.Database import Database
from src.scan.Scan import Scan

def main():
    starting_page = "https://fortcollinschamber.com/resources/small-business-resources/"

    with Crawler(starting_page, "test2.db") as crawler:
        crawler.start()

    #domain = "fortcollinschamber.com"
    #scan = Scan(domain)
    #scan.run_nmap()
    

if __name__ == "__main__":
    main()