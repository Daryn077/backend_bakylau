from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.author_schemas import AuthorDetailSchema
from business_logic.author_service import AuthorService
from data_access.db.session import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/{author_id}", response_model=AuthorDetailSchema)
async def get_author_by_id(
    author_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = AuthorService(db)
    author = await service.get_author_by_id(author_id)

    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return author