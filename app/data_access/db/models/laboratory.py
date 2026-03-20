from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data_access.db.base import Base


class Laboratory(Base):
    __tablename__ = "laboratories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specialization: Mapped[str] = mapped_column(String(255), nullable=False)
    university_id: Mapped[int] = mapped_column(Integer, nullable=False)

    researchers: Mapped[list["Researcher"]] = relationship(
        "Researcher",
        back_populates="laboratory",
        cascade="all, delete-orphan"
    )