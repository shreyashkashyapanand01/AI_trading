# AI Engine (FastAPI)

Production-style MVP intelligence service for AI Trading Coach.

## Endpoints
- `GET /health`
- `POST /api/v1/analyze-stock`
- `POST /api/v1/analyze-trades`
- `POST /api/v1/scan-market`
- `POST /api/v1/analyze-portfolio`

## Internal structure
- `api/`: HTTP contracts
- `schemas/`: request/response models
- `tools/`: data + indicator primitives
- `agents/`: domain reasoning modules
- `analysis/`: scoring and pattern detection
- `pipelines/`: orchestrate feature flows
- `services/`: reusable service logic (scanner)

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Test
```bash
pytest -q
```
