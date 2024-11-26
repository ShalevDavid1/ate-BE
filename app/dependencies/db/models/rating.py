from sqlalchemy import Column, Integer, ForeignKey, Float, CheckConstraint
from app.dependencies.db.models import Base, RATINGS_TABLE_NAME, RESTAURANTS_TABLE_NAME, USERS_TABLE_NAME


class Rating(Base):
    __tablename__ = RATINGS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f'{USERS_TABLE_NAME}.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey(f'{RESTAURANTS_TABLE_NAME}.id'), nullable=False)
    food_rating = Column(Float, nullable=False)
    price_rating = Column(Float, nullable=False)
    service_rating = Column(Float, nullable=False)
    vibe_rating = Column(Float, nullable=False)

    # Add a CheckConstraint to enforce the range
    __table_args__ = (
        CheckConstraint('food_rating >= 1 AND food_rating <= 5', name='check_food_rating_range'),
        CheckConstraint('price_rating >= 1 AND price_rating <= 5', name='check_price_rating_range'),
        CheckConstraint('service_rating >= 1 AND service_rating <= 5', name='check_service_rating_range'),
        CheckConstraint('vibe_rating >= 1 AND vibe_rating <= 5', name='check_vibe_rating_range'),
    )
