from data_access.authors.author_repository import AuthorRepository


class AuthorService:
    def __init__(self, db):
        self.repository = AuthorRepository(db)

    async def get_author_by_id(self, author_id: int):
        return await self.repository.get_author_by_id(author_id)