from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from data_access.db.models.author import Author


class AuthorRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_author_by_id(self, author_id: int) -> Author | None:
        stmt = (
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.id == author_id)
        )
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()