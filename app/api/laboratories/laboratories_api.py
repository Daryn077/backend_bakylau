from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.laboratories.laboratories_schemas import LaboratoryCreate, LaboratoryRead
from business_logic.laboratories.laboratories_service import LaboratoryService
from core.dependencies import get_db
from data_access.laboratories.laboratories_repository import LaboratoryRepository

router = APIRouter()


def get_laboratory_service(db: AsyncSession = Depends(get_db)) -> LaboratoryService:
    repository = LaboratoryRepository(db)
    return LaboratoryService(repository)


@router.get("/", response_model=list[LaboratoryRead])
async def get_laboratories(
    service: LaboratoryService = Depends(get_laboratory_service),
):
    return await service.get_all_laboratories()


@router.get("/{laboratory_id}", response_model=LaboratoryRead)
async def get_laboratory(
    laboratory_id: int,
    service: LaboratoryService = Depends(get_laboratory_service),
):
    return await service.get_laboratory_by_id(laboratory_id)


@router.post("/", response_model=LaboratoryRead, status_code=201)
async def create_laboratory(
    laboratory_data: LaboratoryCreate,
    service: LaboratoryService = Depends(get_laboratory_service),
):
    return await service.create_laboratory(laboratory_data)