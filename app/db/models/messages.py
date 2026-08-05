from datetime import datetime

from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from .enum_models import MessageRole


class Message(Base):
    __tablename__ = "messages"

    message_id: Mapped[int] = mapped_column(primary_key=True)

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.conversation_id"),
        index=True,
    )

    role: Mapped[MessageRole] = mapped_column(SqlEnum(MessageRole))

    content: Mapped[str] = mapped_column(Text)

    message_order: Mapped[int] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())

    conversation = relationship(
        "Conversation",
        back_populates="messages",
    )
