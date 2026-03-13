import asyncio

from sqlalchemy import delete

from data_access.db.models import Author, Book
from data_access.db.session import AsyncSessionLocal


async def seed():
    async with AsyncSessionLocal() as db:
        await db.execute(delete(Book))
        await db.execute(delete(Author))
        await db.commit()

        author1 = Author(
            first_name="Tlegen",
            last_name="Tolstiy",
            birth_year=2005,
        )
        author2 = Author(
            first_name="Make",
            last_name="Doramchik",
            birth_year=2006,
        )

        db.add_all([author1, author2])
        await db.flush()

        books = [
            Book(title="1984", published_year=1949, author_id=author1.id),
            Book(title="Animal Farm", published_year=1945, author_id=author1.id),
            Book(title="Pride and Prejudice", published_year=1813, author_id=author2.id),
        ]

        db.add_all(books)
        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed())