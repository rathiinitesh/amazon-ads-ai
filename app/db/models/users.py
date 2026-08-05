from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base
from app.db.models import Conversation


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(String(255), unique=True)

    full_name: Mapped[str] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())

    conversations: Mapped[list["Conversation"]] = relationship(
        "Conversation",
        back_populates="user",
    )
