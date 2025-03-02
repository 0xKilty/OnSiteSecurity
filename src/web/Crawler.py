import requests
from urllib.parse import urljoin

from .WebUtils import get, get_all_links, get_domain
from .SiteDatabase import SiteDatabase

class Crawler:
    def __init__(self, db_file, starting_page=None):
        self.starting_page = starting_page
        self.db = SiteDatabase(db_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

    def start(self):
        to_visit = {self.starting_page}
        current_url = None

        try:
            while to_visit:
                current_url = to_visit.pop()
                if self.db.is_in(current_url, "visited"):
                    continue
                try:
                    response = get(current_url)
                    if response.status_code != 200:
                        continue

                    for link in get_all_links(response):
                        full_url = urljoin(current_url, link["href"])
                        if full_url.startswith("http") and not self.db.is_in(full_url, "visited"):
                            to_visit.add(full_url)
                    print(len(to_visit), current_url)
                    self.db.add(current_url, "visited")
                except requests.exceptions.RequestException:
                    print("error")
                    continue
        except KeyboardInterrupt:
            pass