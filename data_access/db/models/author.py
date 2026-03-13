from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data_access.db.base import Base


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)

    books: Mapped[list["Book"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan"
    )