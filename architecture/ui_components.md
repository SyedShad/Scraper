# Dashboard UI Architecture

## Theme: Premium Modern (Light Mode)
- **Background:** `#F4F7FE` (Clean, light blue-gray).
- **Cards:** `#FFFFFF` (Pure white).
- **Accents:** `#F27244` (Orange from brand guidelines).
- **Shadows:** Soft, deep shadows (`0px 42px 34px rgba(82, 67, 170, 0.05)`).
- **Typography:** Inter (Sans-serif) with specific weights (700 for headings, 400 for body).

## Components
1. **Sidebar/Navbar:** Minimal, featuring the brand logo and profile mockup.
2. **Dashboard Grid:** Bento-box style with varying card sizes if possible, or a clean cohesive grid.
3. **ArticleCard:**
    - High border-radius (20px).
    - Source badge with solid orange background.
    - Hover state: Subtle lift and shadow intensification.

## State Management
- `useState` for current articles.
- `useEffect` to load data from `.tmp/articles.json` (via a dev proxy or direct fetch if served).
- `localStorage` for the "Saved" state.
