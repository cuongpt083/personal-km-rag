.PHONY: setup up down logs api lint

setup:
	cp -n .env.example .env || true

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f

api:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

lint:
	python -m compileall app

