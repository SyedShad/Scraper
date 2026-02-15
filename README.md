# B.L.A.S.T. Dashboard (AI News Aggregator)

A modern, high-performance AI news dashboard built with React, Vite, and Python. Features a real-time scraping engine and a premium dynamic background powered by Three.js shaders.

## 🚀 Deployment

This repository is optimized for **Vercel** and **Netlify**. Since the configuration files are in the root directory, you can simply import this repository and it will deploy automatically.

- **Vercel**: Just link your GitHub repo.
- **Netlify**: Just link your GitHub repo.

## ✨ Features

- **Multi-Source Scraping**: Aggregates AI news from Reddit, Ben's Bites, and The Rundown AI.
- **Premium UI**: Dynamic "Dot-Shader" background with reactive mouse trail effects.
- **Save System**: Persistently save articles to your local collection.
- **Stats Overview**: Real-time article and saved count indicators.

## 🛠️ Local Development

### Dashboard (Frontend)
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run the development server:
   ```bash
   npm run dev
   ```

### Scraper (Backend Tools)
1. Navigate to the `tools` directory.
2. Run the aggregator to update `public/articles.json`:
   ```bash
   python tools/aggregator.py
   ```

## 📄 Repository Structure

- `/src`: React frontend source code.
- `/public`: Static assets (including the scraped `articles.json`).
- `/tools`: Python scraping scripts.
- `package.json`: Main project configuration.
- `vite.config.ts`: Vite build configuration.
