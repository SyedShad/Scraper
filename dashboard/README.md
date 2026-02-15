# B.L.A.S.T. Dashboard (AI News Aggregator)

A modern, high-performance AI news dashboard built with React, Vite, and Python. Features a real-time scraping engine and a premium dynamic background powered by Three.js shaders.

## 🚀 Tech Stack

- **Frontend**: React 19, Vite, TypeScript
- **Styling**: Tailwind CSS v4
- **Graphics**: Three.js (React Three Fiber/Drei)
- **Scraper**: Python (Requests, BeautifulSoup, Datetime)

## ✨ Features

- **Multi-Source Scraping**: Aggregates AI news from Reddit, Ben's Bites, and The Rundown AI.
- **Premium UI**: Dynamic "Dot-Shader" background with reactive mouse trail effects.
- **Save System**: Persistently save articles to your local collection.
- **Stats Overview**: Real-time article and saved count indicators.
- **Smart Filtering**: Automatic filtering to ensure articles have high-quality images.

## 🛠️ Setup

### Frontend (Dashboard)
1. Navigate to the `dashboard` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

### Scraper (Tools)
1. Navigate to the `tools` directory.
2. Run the aggregator:
   ```bash
   python aggregator.py
   ```
   *Note: This will fetch the latest news and update `dashboard/public/articles.json`.*

## 📄 Repository Structure

- `/dashboard`: React frontend source code.
- `/tools`: Python scraping scripts.
- `/Design Guidelines`: Project assets and brand information.
