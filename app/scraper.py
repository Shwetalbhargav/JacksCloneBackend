import requests
from bs4 import BeautifulSoup

def scrape_jackjay():
    url = "https://www.jackjay.io"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the website. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract data (Example: Titles and descriptions of blog posts)
    data = []
    for article in soup.find_all("article"):
        title = article.find("h2").get_text(strip=True)
        description = article.find("p").get_text(strip=True)
        data.append({
            "title": title,
            "description": description
        })
    
    return data
