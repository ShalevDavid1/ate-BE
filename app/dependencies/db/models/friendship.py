from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint, UniqueConstraint
from app.dependencies.db.models import Base, FRIENDSHIPS_TABLE_NAME, USERS_TABLE_NAME


class Friendship(Base):
    __tablename__ = FRIENDSHIPS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f'{USERS_TABLE_NAME}.id'), nullable=False)
    friend_id = Column(Integer, ForeignKey(f'{USERS_TABLE_NAME}.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'friend_id', name='unique_friendship'),
        CheckConstraint('user_id != friend_id', name='no_self_friendship')
    )
