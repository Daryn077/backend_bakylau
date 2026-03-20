from fastapi import APIRouter
from api.laboratories.laboratories_router import router as laboratories_router

api_router = APIRouter()

api_router.include_router(
    laboratories_router,
    prefix="/api",
)