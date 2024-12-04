from app.crud.restaurant import get_restaurants, add_rated_restaurant
from app.schemas.restaurant import RatedRestaurant, RatedRestaurantCreate
from app.dependencies.db.db_connection import DatabaseConnection
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.user import get_user

router = APIRouter()


@router.get("/", response_model=list[RatedRestaurant])
def get_restaurants_route(email: str, skip: int = 0, limit: int = None,
                          db: Session = Depends(DatabaseConnection.get_db)):
    """
    Get a list of all restaurants.
    Supports pagination using `skip` and `limit`.
    """
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=400, detail="Email is not registered")

    restaurants = get_restaurants(db, user.id, skip=skip, limit=limit)
    formatted_restaurants = [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "formatted_address": restaurant.formatted_address,
            "lat": restaurant.lat,
            "lng": restaurant.lng,
            "icon": restaurant.icon,
            "rating": {
                "price_rating": rating.price_rating,
                "service_rating": rating.service_rating,
                "food_rating": rating.food_rating,
                "vibe_rating": rating.vibe_rating,
            },
        }
        for restaurant, rating in restaurants
    ]
    return formatted_restaurants


@router.post("/add_rated_restaurant")
def add_rated_restaurant_route(email: str, rated_restaurant: RatedRestaurantCreate,
                               db: Session = Depends(DatabaseConnection.get_db)):
    """
    Gets user_email: str, and restaurant_with_rating: RatedRestaurantCreate
    And adds it to the Restaurant & Rating DB schemas
    """

    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=400, detail="Email is not registered")

    user_id = user.id
    added_restaurant = add_rated_restaurant(db, user_id, rated_restaurant)
    return added_restaurant
