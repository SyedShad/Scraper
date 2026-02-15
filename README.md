# B.L.A.S.T. (AI News Aggregator & Dashboard)

A high-performance AI news dashboard with a dynamic Three.js background and Python-powered scrapers.

## 🏗 Project Structure

- **[/dashboard](./dashboard)**: React 19 + Vite + Tailwind CSS v4 frontend.
- **[/tools](./tools)**: Python scrapers for Reddit, Ben's Bites, and The Rundown AI.
- **[/architecture](./architecture)**: Documentation on SOPs and UI components.

## 🚀 Deployment

This project is configured for **Vercel**. 
1. Connect this repository to Vercel.
2. The `vercel.json` in the root will automatically handle the subdirectory build.
3. Your dashboard will be live!

## 🛠 Local Development

### Dashboard
```bash
cd dashboard
npm install
npm run dev
```

### Scraper
```bash
cd tools
python aggregator.py
```
