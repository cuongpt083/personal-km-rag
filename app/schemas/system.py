from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app: str
    environment: str


class RuntimeConfigResponse(BaseModel):
    postgres_dsn: str
    qdrant_url: str
    qdrant_collection: str

