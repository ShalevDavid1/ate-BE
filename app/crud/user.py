from app.dependencies.db.models.user import User
from sqlalchemy.orm import Session
from typing import Optional


def create_user(db: Session, user_name: str, email: str) -> User:
    new_user = User(
        username=user_name,
        email=email
    )
    # Add and commit the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
