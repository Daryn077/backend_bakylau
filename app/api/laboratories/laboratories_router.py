from fastapi import APIRouter
from . import laboratories_api

router = APIRouter(
    prefix="/laboratories",
)

router.include_router(
    laboratories_api.router,
    tags=["laboratories"],
)