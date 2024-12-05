from app.dependencies.db.models.friendship import Friendship
from app.dependencies.db.models.user import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def get_friends(db: Session, user_id: int):
    return db.query(User.id, User.email, User.username) \
        .join(Friendship, Friendship.friend_id == User.id) \
        .filter(Friendship.user_id == user_id) \
        .all()


def get_friendship(db: Session, user_id: int, friend_id: int):
    return db.query(Friendship)\
        .filter((Friendship.user_id == user_id)
                & (Friendship.friend_id == friend_id))\
        .first()


def add_friendship(db: Session, user_id: int, friend_id: int):
    try:
        friendship = Friendship(user_id=user_id, friend_id=friend_id)
        db.add(friendship)

        reverse_friendship = Friendship(user_id=friend_id, friend_id=user_id)
        db.add(reverse_friendship)

        db.commit()
        return {"message": "Friendship successfully added."}
    except IntegrityError:  # caught to handle cases where the friendship already exists
        # or violates database constraints.
        db.rollback()
        return {"error": "Friendship already exists or another database error occurred."}
