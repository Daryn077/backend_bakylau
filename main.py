from fastapi import FastAPI

from api.author_router import router as author_router
from api.book_router import router as book_router
from core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(author_router)
app.include_router(book_router)