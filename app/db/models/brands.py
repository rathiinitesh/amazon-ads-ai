from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Brand(Base):
    __tablename__ = "brands"

    brand_id: Mapped[int] = mapped_column(primary_key=True)
    brand_name: Mapped[str] = mapped_column(String(100), unique=True)
    brand_owner: Mapped[str] = mapped_column(String(150), nullable=True)
    country_of_origin: Mapped[str] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())

    products = relationship("Product", back_populates="brand")
