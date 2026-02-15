import requests
import json
from datetime import datetime, timedelta, timezone
import os

def fetch_reddit_ai():
    # Use hot and increase limit to get more potential articles with images
    url = "https://www.reddit.com/r/ArtificialInteligence/hot.json?limit=50"
    headers = {
        "User-Agent": "AntigravityScraper/1.0 (Educational Dashboard Project)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        articles = []
        now = datetime.now(timezone.utc)
        
        for post in data.get("data", {}).get("children", []):
            item = post.get("data", {})
            
            # Use created_utc for publication time
            published_at = datetime.fromtimestamp(item.get("created_utc"), tz=timezone.utc)
            
            # Expanded image detection
            image_url = None
            
            # 1. Check preview images (highest quality)
            preview = item.get("preview", {}).get("images", [])
            if preview:
                try:
                    image_url = preview[0]["source"]["url"].replace("&amp;", "&")
                except (IndexError, KeyError):
                    pass
            
            # 2. Check thumbnail if it's a real URL
            if not image_url and item.get("thumbnail") and item.get("thumbnail").startswith("http"):
                image_url = item.get("thumbnail")
            
            # 3. Check if it's an image post directly
            if not image_url and item.get("post_hint") == "image":
                image_url = item.get("url")
                
            # 4. Check url_overridden_by_dest for common image extensions
            if not image_url:
                dest_url = item.get("url_overridden_by_dest", "")
                if any(dest_url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"]):
                    image_url = dest_url

            articles.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "subtitle": f"u/{item.get('author')} in r/{item.get('subreddit')}",
                "summary": item.get("selftext")[:200] + "..." if item.get("selftext") else "Reddit Discussion",
                "url": f"https://www.reddit.com{item.get('permalink')}",
                "image_url": image_url,
                "source": "Reddit",
                "published_at": published_at.isoformat(),
                "category": "Social",
                "saved": False,
                "scraped_at": now.isoformat()
            })
        
        return articles
    except Exception as e:
        print(f"Error fetching Reddit: {e}")
        return []

if __name__ == "__main__":
    results = fetch_reddit_ai()
    print(json.dumps(results, indent=2))
