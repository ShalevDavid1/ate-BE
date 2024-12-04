from app.schemas.rating import RestaurantRatingOptions, Rating
from pydantic import BaseModel
from typing import Optional


class RestaurantBase(BaseModel):
    name: str
    formatted_address: str
    lat: float
    lng: float
    icon: Optional[str] = None


class RatedRestaurantCreate(RestaurantBase):
    rating: RestaurantRatingOptions


class Restaurant(RestaurantBase):
    id: int

    class Config:
        orm_mode = True


class RatedRestaurant(Restaurant):
    rating: RestaurantRatingOptions
