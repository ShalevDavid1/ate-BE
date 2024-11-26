from sqlalchemy import Column, Integer, String
from app.dependencies.db.models import Base, USERS_TABLE_NAME


class User(Base):
    __tablename__ = USERS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
