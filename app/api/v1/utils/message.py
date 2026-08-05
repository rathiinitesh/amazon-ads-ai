from app.db.models import Message
from app.db.models.enum_models import MessageRole
from app.db.session import SessionLocal


def create_message(
    conversation_id: int, role: str, content: str | None, message_order: int = 1
):
    db = SessionLocal()

    db_message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
        message_order=message_order,
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def update_message(
    conversation_id: int,
    content: str | None,
    role: str | None,
    message_order: int,
    message_id: int,
):
    db = SessionLocal()
    db_message = (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id, Message.message_id == message_id
        )
        .first()
    )

    if not db_message:
        return None

    if db_message.conversation_id != conversation_id:
        return None

    if content is not None:
        db_message.content = content

    if role is not None:
        db_message.role = MessageRole(role.upper())

    if message_order is not None:
        db_message.message_order = message_order

    db.commit()
    db.refresh(db_message)
    return db_message


def get_message_by_id(
    conversation_id: int,
    message_id: int | None = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
):
    db = SessionLocal()
    db_message = (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(getattr(getattr(Message, sort_by), sort_order)())
        .first()
    )
    return db_message
