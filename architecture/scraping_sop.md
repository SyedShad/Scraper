# Scraping SOP

## Goal
Extract AI-related articles from Ben's Bites, The Rundown AI, and Reddit from the last 24 hours.

## Source 1: Ben's Bites
- **Endpoint:** `https://bensbites.beehiiv.com/posts`
- **Logic:**
    1. Fetch the JSON from the `/posts` endpoint.
    2. Iterate through `posts`.
    3. Filter by `created_at` matching the last 24 hours.
    4. Map to standardized payload.

## Source 2: The Rundown AI
- **Endpoint:** `https://therundown.ai/archive`
- **Logic:**
    1. Fetch HTML using `requests`.
    2. Use `BeautifulSoup` to find article links (likely `<a>` tags with `/p/` prefix).
    3. Filter by date/recency.
    4. Map to standardized payload.

## Source 3: Reddit
- **Endpoint:** `https://www.reddit.com/r/ArtificialInteligence/top.json?t=day`
- **Logic:**
    1. Call the JSON API.
    2. Extract `data.children`.
    3. Map fields: `title`, `url`, `selftext` (as summary).

## Error Handling
- Use retry logic for network timeouts.
- If a source fails, log the error to `progress.md` and continue with other sources.
