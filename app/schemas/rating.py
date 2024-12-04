from pydantic import BaseModel, confloat


class RestaurantRatingOptions(BaseModel):
    food_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    price_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    service_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    vibe_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0


class RatingBase(RestaurantRatingOptions):
    user_id: int
    restaurant_id: int


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    food_rating: confloat(ge=1.0, le=5.0)
    price_rating: confloat(ge=1.0, le=5.0)
    service_rating: confloat(ge=1.0, le=5.0)
    vibe_rating: confloat(ge=1.0, le=5.0)


class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True
