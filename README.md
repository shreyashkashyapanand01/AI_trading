# AI Trading Coach

This repository now contains a complete MVP implementation of the **AI engine** layer and architecture docs for the platform.

## Implemented capabilities
1. **Stock Decision Advisor** (`/api/v1/analyze-stock`)
   - trend, momentum, RSI, volatility, sentiment, fundamentals
   - explainable summary + risk level + confidence
2. **Trade Behaviour Analyzer** (`/api/v1/analyze-trades`)
   - computes behavior metrics
   - detects common mistakes (revenge trading, inconsistent size, etc.)
   - returns coaching suggestions
3. **Opportunity Finder** (`/api/v1/scan-market`)
   - scans predefined universes
   - ranks opportunities by scored setup quality
4. **Portfolio Monitoring** (`/api/v1/analyze-portfolio`)
   - analyzes each holding’s daily movement and unrealized PnL context
   - labels risk-increasing vs improving conditions

## Architecture
- `ai-engine-python/`: implemented FastAPI intelligence layer
- `backend-springboot/`: orchestration-layer notes and integration target
- `docs/`: project scope and phased build details

## Quick start
```bash
cd ai-engine-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Validation
```bash
cd ai-engine-python
pytest -q
```
