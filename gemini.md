# Gemini: Project Constitution

# Gemini: Project Constitution

## Data Schemas

### Article Payload
```json
{
  "id": "string (uuid or hash)",
  "title": "string",
  "subtitle": "string (optional)",
  "summary": "string",
  "url": "string",
  "image_url": "string (optional)",
  "source": "string (Ben's Bytes | AI Rundown | Reddit)",
  "published_at": "ISO8601",
  "category": "string",
  "saved": "boolean",
  "scraped_at": "ISO8601"
}
```

## Discovery Answers
- **North Star:** Interactive dashboard showcasing latest AI news from 24h.
- **Integrations:** Custom Python Scrapers, Supabase (Phase 2/3), Interactive Frontend.
- **Source of Truth:** [bensbytes.beehiiv.com](https://bensbytes.beehiiv.com), [therundown.ai](https://therundown.ai), [reddit.com/r/ArtificialInteligence](https://reddit.com/r/ArtificialInteligence).
- **Delivery Payload:** Dynamic Dashboard with "Save" functionality.
- **Behavioral Rules:** Gorgeous aesthetics, interactive UI, 24h refresh cycle.

## Behavioral Rules
- **Protocol:** B.L.A.S.T. (Blueprint, Link, Architect, Stylize, Trigger)
- **Architecture:** A.N.T. 3-Layer (Architecture, Navigation, Tools)
- **Reliability First:** Prioritize deterministic behavior over speed.
- **No Guessing:** Do not invent business logic.
- **Self-Healing:** Update SOPs on failure.

## Architectural Invariants
- **Layer 1 (Architecture):** SOPs live in `architecture/`.
- **Layer 2 (Navigation):** Reasoning and routing.
- **Layer 3 (Tools):** Atomic scripts in `tools/`.
- **Intermediates:** All temporary data stored in `.tmp/`.
- **UI:** Modern, premium aesthetics using Vite + Vanilla CSS/React.

## Maintenance Log
*No activities yet.*
