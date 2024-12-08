import requests
from bs4 import BeautifulSoup

def scrape_jackjay():
    try:
        url = "https://www.jackjay.io"
        response = requests.get(url, timeout=10)  # Add timeout
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch the website. Status code: {response.status_code}")
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        data = []
        for article in soup.find_all("article"):
            title = article.find("h2").get_text(strip=True)
            description = article.find("p").get_text(strip=True)
            data.append({"title": title, "description": description})
        
        return data
    except Exception as e:
        raise Exception(f"Error during scraping: {str(e)}")
