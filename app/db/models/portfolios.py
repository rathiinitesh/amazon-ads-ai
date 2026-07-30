from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy.sql import func


from app.db.base import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    portfolio_id: Mapped[int] = mapped_column(primary_key=True)
    portfolio_name: Mapped[str] = mapped_column(String(100))
    manager_name: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())
