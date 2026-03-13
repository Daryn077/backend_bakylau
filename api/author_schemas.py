from typing import List
from pydantic import BaseModel


class BookInAuthorSchema(BaseModel):
    id: int
    title: str
    published_year: int

    class Config:
        from_attributes = True


class AuthorDetailSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_year: int
    books: List[BookInAuthorSchema] = []

    class Config:
        from_attributes = True