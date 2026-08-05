from app.db.models.users import User
from app.db.session import SessionLocal


def create_user(email: str, full_name: str):
    db = SessionLocal()

    db_user = User(email=email, full_name=full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, email: str | None, full_name: str | None):
    db = SessionLocal()
    db_user = db.query(User).filter(User.user_id == user_id).first()

    if not db_user:
        return None

    if email:
        db_user.email = email
    if full_name:
        db_user.full_name = full_name

    db.commit()
    db.refresh(db_user)
    return db_user
