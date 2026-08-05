from datetime import datetime

from app.db.models.users import Conversation
from app.db.session import SessionLocal


def create_conversation(user_id: int, title: str):
    db = SessionLocal()

    db_conversation = Conversation(user_id=user_id, title=title)
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation


def update_conversation(conversation_id: int, user_id: int, title: str):
    db = SessionLocal()
    db_conversation = (
        db.query(Conversation)
        .filter(Conversation.conversation_id == conversation_id)
        .first()
    )

    if not db_conversation or db_conversation.user_id != user_id:
        return None

    if title:
        db_conversation.title = title
    db_conversation.updated_at = datetime.now()  # noqa: DTZ005

    db.commit()
    db.refresh(db_conversation)
    return db_conversation
