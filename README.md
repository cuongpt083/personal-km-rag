# personal-km-rag

Personal Knowledge Management System using RAG.

## Day 1 Bootstrap

Day 1 scope implemented:
- Backend skeleton with `FastAPI`
- Local infrastructure with `PostgreSQL` and `Qdrant`
- Centralized environment config (`.env.example`)
- Base API route: `/api/v1/health`

## Project Structure

```text
app/
  api/
  core/
  schemas/
  services/
docs/
docker-compose.yml
Dockerfile
Makefile
requirements.txt
```

## Quick Start

1. Create env file:
```bash
make setup
```

2. Start services:
```bash
make up
```

3. Verify API:
```bash
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/api/v1/system/config
```

4. Stop services:
```bash
make down
```

## Notes

- Default stack: `FastAPI + PostgreSQL + Qdrant`
- Runtime config is loaded via `pydantic-settings` from `.env`
- Next step is Day 2 ingestion pipeline implementation
