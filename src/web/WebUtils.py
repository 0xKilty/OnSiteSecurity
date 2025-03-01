import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def get(current_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(current_url, timeout=5, headers=headers)
    return response

def get_all_links(response):
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("a", href=True)
