import requests
from urllib.parse import urljoin

from .WebUtils import get, get_all_links

class Crawler:
    def __init__(self, starting_page):
        self.starting_page = starting_page

    def start(self):
        visited = set()
        to_visit = [self.starting_page]

        while to_visit:
            current_url = to_visit.pop(0)
            print(current_url)
            if current_url in visited:
                continue
            try:
                response = get(current_url)
                if response.status_code != 200:
                    continue

                for link in get_all_links(response):
                    full_url = urljoin(current_url, link["href"])
                    if full_url not in visited and full_url.startswith("http"):
                        to_visit.append(full_url)
                        
                visited.add(current_url)
            except requests.exceptions.RequestException:
                print("error")
                continue  