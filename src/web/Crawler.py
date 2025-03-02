import requests
from urllib.parse import urljoin

from .WebUtils import get, get_all_links, get_domain
from .SiteDatabase import SiteDatabase

class Crawler:
    def __init__(self, starting_page, db_file):
        self.starting_page = starting_page
        self.db = SiteDatabase(db_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

    def start(self):
        to_visit = {self.starting_page}

        while to_visit:
            current_url = to_visit.pop()
            if self.db.has_visited(current_url):
                continue
            try:
                response = get(current_url)
                if response.status_code != 200:
                    continue

                for link in get_all_links(response):
                    full_url = urljoin(current_url, link["href"])
                    if not self.db.has_visited(full_url) and full_url.startswith("http"):
                        to_visit.add(full_url)
                print(len(to_visit), current_url)
                self.db.add_site(current_url)
            except requests.exceptions.RequestException:
                print("error")
                continue