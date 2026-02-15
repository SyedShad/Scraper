import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone
import os

def fetch_rundown_ai():
    url = "https://therundown.ai/archive"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        articles = []
        now = datetime.now(timezone.utc)
        
        # The Rundown AI archive links are usually within specific blocks
        # Based on previous research, they start with /p/
        links = soup.find_all("a", href=True)
        
        seen_urls = set()
        for link in links:
            href = link['href']
            if href.startswith("/p/") and href not in seen_urls:
                seen_urls.add(href)
                # Title is usually inside the link or nearby
                title = link.get_text(strip=True)
                if len(title) < 10: continue # Skip "Load more" etc.
                
                # Attempt to find an image in the parent container
                image_url = None 
                
                # Check if the link itself or a nearby img tag has a src
                parent = link.find_parent("div")
                if parent:
                    img = parent.find("img")
                    if img and img.get("src"):
                        image_url = img["src"]

                articles.append({
                    "id": href.split("/")[-1],
                    "title": title,
                    "subtitle": "Daily AI News",
                    "summary": "Full update from The Rundown AI",
                    "url": f"https://therundown.ai{href}",
                    "image_url": image_url,
                    "source": "The Rundown AI",
                    "published_at": now.isoformat(),
                    "category": "Newsletter",
                    "saved": False,
                    "scraped_at": now.isoformat()
                })
                
                    
        return articles
    except Exception as e:
        print(f"Error fetching The Rundown: {e}")
        return []

if __name__ == "__main__":
    results = fetch_rundown_ai()
    print(json.dumps(results, indent=2))
