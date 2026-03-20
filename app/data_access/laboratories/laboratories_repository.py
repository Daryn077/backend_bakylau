from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from data_access.db.models.laboratory import Laboratory


class LaboratoryRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(
            select(Laboratory).options(selectinload(Laboratory.researchers))
        )
        return result.scalars().all()

    async def get_by_id(self, laboratory_id: int):
        result = await self.db.execute(
            select(Laboratory)
            .options(selectinload(Laboratory.researchers))
            .where(Laboratory.id == laboratory_id)
        )
        return result.scalar_one_or_none()

    async def create(self, laboratory: Laboratory):
        self.db.add(laboratory)
        await self.db.commit()
        await self.db.refresh(laboratory)
        return laboratory