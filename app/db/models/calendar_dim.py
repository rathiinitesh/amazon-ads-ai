from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime

from app.db.base import Base


class CalendarDim(Base):
    __tablename__ = "calendar_dim"

    calendar_date: Mapped[datetime.date] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column()
    quarter: Mapped[int] = mapped_column()
    month: Mapped[int] = mapped_column()
    month_name: Mapped[str] = mapped_column(String(20))
    week_of_year: Mapped[int] = mapped_column()
    day_of_month: Mapped[int] = mapped_column()
    day_name: Mapped[str] = mapped_column(String(20))
    is_weekend: Mapped[bool] = mapped_column()
    is_prime_day: Mapped[bool] = mapped_column()
    is_black_friday: Mapped[bool] = mapped_column()
    is_cyber_monday: Mapped[bool] = mapped_column()
    is_christmas: Mapped[bool] = mapped_column()
    currency: Mapped[str] = mapped_column(String(10))
