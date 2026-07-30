from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class Marketplace(Base):
    __tablename__ = "marketplaces"

    marketplace_id: Mapped[int] = mapped_column(primary_key=True)
    marketplace_code: Mapped[str] = mapped_column(String(10), unique=True)
    marketplace_name: Mapped[str] = mapped_column(String(100))
    currency: Mapped[str] = mapped_column(String(10))
