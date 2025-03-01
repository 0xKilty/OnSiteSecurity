import requests

def get(current_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(current_url, timeout=5, headers=headers)
    return response

def some(soup, visited, to_visit, current_url):
    for link in soup.find_all("a", href=True):
        full_url = urljoin(current_url, link["href"])
        if full_url not in visited and full_url.startswith("http"):
            to_visit.append(full_url)