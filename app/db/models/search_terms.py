from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SearchTerm(Base):
    __tablename__ = "search_terms"

    search_term_id: Mapped[int] = mapped_column(primary_key=True)
    search_term: Mapped[str] = mapped_column(String(255))
    search_volume: Mapped[int] = mapped_column()
    competition: Mapped[str] = mapped_column(String(10))
