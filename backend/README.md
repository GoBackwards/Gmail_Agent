# Gmail Agent Backend

Simple FastAPI scaffold for local development.

## Requirements
- Python 3.11+

## Setup & Run
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Example Requests
Health check:
```bash
curl http://localhost:8000/health
```

Analyze request:
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "email_text": "Hello from the Gmail Agent backend.",
    "metadata": {"source": "manual"}
  }'
```
