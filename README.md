# Wukong Math Quest - AI Children's Educational Game

A web-based educational game for children aged 4-6, featuring Sun Wukong (Monkey King)
from Journey to the West. Built with FastAPI + React + AI-generated content.

## Architecture

```
┌──────────────────────┐
│  AI Level Generator  │  ← Claude/OpenAI API
│  (Python/FastAPI)    │
└──────────┬───────────┘
           │ JSON
┌──────────▼───────────┐
│  FastAPI Backend      │  ← Level API, Progress Tracking
│  /api/levels          │
│  /api/progress        │
└──────────┬───────────┘
           │ REST
┌──────────▼───────────┐
│  React Game Frontend  │  ← PixiJS/Canvas Games
│  10 Game Components   │
└──────────┬───────────┘
           │
    Mobile / Web Browser
```

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
wukong/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry
│   │   ├── api/
│   │   │   ├── levels.py        # Level endpoints
│   │   │   └── progress.py      # Progress endpoints
│   │   ├── core/
│   │   │   ├── level_generator.py  # AI level generation
│   │   │   └── config.py
│   │   └── models/
│   │       └── schemas.py       # Pydantic models
│   ├── data/
│   │   └── levels.json          # 100 pre-built levels
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── games/           # 10 game type components
│   │   │   └── ui/              # Shared UI components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── stores/              # State management
│   │   └── types/               # TypeScript types
│   └── package.json
└── README.md
```
