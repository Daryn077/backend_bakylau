from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    published_year: int
    author_id: int

    class Config:
        from_attributes = True