from fastapi import HTTPException

from api.laboratories.laboratories_schemas import LaboratoryCreate
from data_access.db.models.laboratory import Laboratory
from data_access.laboratories.laboratories_repository import LaboratoryRepository


class LaboratoryService:
    def __init__(self, repository: LaboratoryRepository):
        self.repository = repository

    async def get_all_laboratories(self):
        return await self.repository.get_all()

    async def get_laboratory_by_id(self, laboratory_id: int):
        laboratory = await self.repository.get_by_id(laboratory_id)
        if laboratory is None:
            raise HTTPException(status_code=404, detail="Laboratory not found")
        return laboratory

    async def create_laboratory(self, laboratory_data: LaboratoryCreate):
        laboratory = Laboratory(
            name=laboratory_data.name,
            specialization=laboratory_data.specialization,
            university_id=laboratory_data.university_id,
        )
        return await self.repository.create(laboratory)