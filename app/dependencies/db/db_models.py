from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, \
    CheckConstraint, UniqueConstraint

# Define the base for our models
Base = declarative_base()

USERS_TABLE_NAME = "users"
RESTAURANTS_TABLE_NAME = "restaurants"
RATINGS_TABLE_NAME = "ratings"
FRIENDSHIPS_TABLE_NAME = "friendships"


class User(Base):
    __tablename__ = USERS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Restaurant(Base):
    __tablename__ = RESTAURANTS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    formatted_address = Column(String)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    icon = Column(String)


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


class Friendship(Base):
    __tablename__ = FRIENDSHIPS_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(f'{USERS_TABLE_NAME}.id'), nullable=False)
    friend_id = Column(Integer, ForeignKey(f'{USERS_TABLE_NAME}.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'friend_id', name='unique_friendship'),
        CheckConstraint('user_id != friend_id', name='no_self_friendship')
    )


if __name__ == "__main__":
    # Create tables if they don't exist
    from db_connection import DatabaseConnection

    Base.metadata.create_all(bind=DatabaseConnection.get_engine())

    # Using the singleton session to interact with the database
    # db = DatabaseConnection.get_db()  # Get the singleton session
    db = DatabaseConnection.get_session()  # Get the singleton session
    # user = User(username="shalevd20144", email="shalevd20144@gmail.com")
    # db.add(user)
    # db.commit()
    # db.refresh(user)

    # for res in restraunts:
    #     restaurant = Restaurant(formatted_address=res["formatted_address"],
    #                             name=res["name"],
    #                             lat=res["geometry"]["location"]["lat"],
    #                             lng=res["geometry"]["location"]["lng"],
    #                             icon=res["icon"])
    #     db.add(restaurant)
    #     db.commit()
    #     db.refresh(restaurant)

    # print(f"User created: {user.id}, {user.username}, {user.email}")
