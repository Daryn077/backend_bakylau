from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data_access.db.base import Base


class Researcher(Base):
    __tablename__ = "researchers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    degree: Mapped[str] = mapped_column(String(255), nullable=False)
    laboratory_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("laboratories.id", ondelete="CASCADE"),
        nullable=False,
    )

    laboratory: Mapped["Laboratory"] = relationship(
        "Laboratory",
        back_populates="researchers"
    )