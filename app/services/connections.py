from qdrant_client import QdrantClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import Settings


def create_postgres_engine(settings: Settings) -> Engine:
    return create_engine(settings.postgres_dsn, pool_pre_ping=True)


def create_qdrant_client(settings: Settings) -> QdrantClient:
    return QdrantClient(url=settings.qdrant_url)

