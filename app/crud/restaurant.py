from app.dependencies.db.models.restaurant import Restaurant
from app.dependencies.db.models.rating import Rating
from app.schemas.restaurant import RatedRestaurant
from sqlalchemy.orm import Session


def get_restaurants(db: Session, user_id: int, skip: int = 0, limit: int = None):
    query = db.query(Restaurant, Rating) \
        .join(Rating, Restaurant.id == Rating.restaurant_id) \
        .filter(Rating.user_id == user_id)
    query = query.offset(skip)
    if limit is not None:
        query = query.limit(limit)
    return query.all()


def add_rated_restaurant(db: Session, user_id: int, rated_restaurant: RatedRestaurant):
    restaurant_dict = rated_restaurant.dict()
    restaurant_rating = restaurant_dict.pop("rating")

    restaurant = Restaurant(**restaurant_dict)

    db.add(restaurant)  # Add the restaurant first to generate its ID
    db.flush()  # Generates the ID without committing

    rating = Rating(
        restaurant_id=restaurant.id,
        user_id=user_id,
        **restaurant_rating)

    db.add(rating)
    db.commit()

    added_restaurant = rated_restaurant.dict()
    added_restaurant["id"] = restaurant.id
    return added_restaurant
