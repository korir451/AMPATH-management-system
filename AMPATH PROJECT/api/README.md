# AMPATH API (FastAPI)

## Local run
1) Start Postgres:
- `docker compose up -d`

2) Create env:
- copy `.env.example` to `.env`

3) Run API:
- `python -m uvicorn app.main:app --reload --port 8000`

Swagger docs:
- http://localhost:8000/docs

