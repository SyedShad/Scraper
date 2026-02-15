import json
import os
from datetime import datetime
from scraper_bens import fetch_bens_bites
from scraper_reddit import fetch_reddit_ai
from scraper_rundown import fetch_rundown_ai

def main():
    print("🚀 Starting AI News Aggregator...")
    
    all_articles = []
    
    # Fetch from all sources
    print("fetching Ben's Bites...")
    all_articles.extend(fetch_bens_bites())
    
    print("fetching Reddit...")
    all_articles.extend(fetch_reddit_ai())
    
    print("fetching The Rundown AI...")
    all_articles.extend(fetch_rundown_ai())
    
    # deduplicate by URL
    unique_articles = {}
    for art in all_articles:
        unique_articles[art['url']] = art
        
    final_list = list(unique_articles.values())

    # Filter: Only keep articles with images
    final_list = [art for art in final_list if art.get("image_url") and art["image_url"].strip() != ""]
    
    # Sort by published_at (newest first)
    final_list.sort(key=lambda x: x['published_at'], reverse=True)
    
    # Save directly to public directory
    output_path = "public/articles.json"
    with open(output_path, "w") as f:
        json.dump(final_list, f, indent=2)
        
    print(f"✅ Aggregation complete. Saved {len(final_list)} articles with images to {output_path}")

if __name__ == "__main__":
    main()
