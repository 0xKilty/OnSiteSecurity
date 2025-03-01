import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .WebUtils import get

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

                soup = BeautifulSoup(response.text, "html.parser")
                for link in soup.find_all("a", href=True):
                    full_url = urljoin(current_url, link["href"])
                    if full_url not in visited and full_url.startswith("http"):
                        to_visit.append(full_url)
                visited.add(current_url)
            except requests.exceptions.RequestException:
                print("error")
                continue  