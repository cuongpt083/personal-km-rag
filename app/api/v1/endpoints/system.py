from fastapi import APIRouter

from app.core.config import get_settings
from app.schemas.system import HealthResponse, RuntimeConfigResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(status="ok", app=settings.app_name, environment=settings.app_env)


@router.get("/system/config", response_model=RuntimeConfigResponse)
def runtime_config() -> RuntimeConfigResponse:
    settings = get_settings()
    return RuntimeConfigResponse(
        postgres_dsn=settings.postgres_dsn,
        qdrant_url=settings.qdrant_url,
        qdrant_collection=settings.qdrant_collection,
    )

