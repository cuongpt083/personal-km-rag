from fastapi import APIRouter

from app.api.v1.endpoints.system import router as system_router

api_router = APIRouter()
api_router.include_router(system_router, tags=["system"])

