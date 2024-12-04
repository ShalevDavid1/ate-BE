from sqlalchemy import Column, Integer, String, Float
from app.dependencies.db.models import Base, RESTAURANTS_TABLE_NAME


class Restaurant(Base):
    __tablename__ = RESTAURANTS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    formatted_address = Column(String)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    icon = Column(String, nullable=True)
