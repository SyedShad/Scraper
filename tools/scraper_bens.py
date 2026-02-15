import requests
import json
from datetime import datetime, timedelta, timezone
import os

def fetch_bens_bites():
    url = "https://bensbites.beehiiv.com/posts"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://bensbites.beehiiv.com/",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        articles = []
        now = datetime.now(timezone.utc)
        cutoff = now - timedelta(hours=72)
        
        for post in data.get("posts", []):
            published_at_str = post.get("created_at")
            if not published_at_str:
                continue
                
            published_at = datetime.fromisoformat(published_at_str.replace("Z", "+00:00"))
            
            if published_at >= cutoff:
                articles.append({
                    "id": post.get("id"),
                    "title": post.get("web_title"),
                    "subtitle": post.get("web_subtitle"),
                    "summary": post.get("web_subtitle") or post.get("web_title"),
                    "url": f"https://bensbites.beehiiv.com/p/{post.get('slug')}",
                    "image_url": post.get("image_url"),
                    "source": "Ben's Bites",
                    "published_at": published_at_str,
                    "category": "Newsletter",
                    "saved": False,
                    "scraped_at": now.isoformat()
                })
        
        return articles
    except Exception as e:
        print(f"Error fetching Ben's Bites: {e}")
        return []

if __name__ == "__main__":
    results = fetch_bens_bites()
    print(json.dumps(results, indent=2))
