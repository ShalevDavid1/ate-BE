from pydantic import BaseModel, confloat

food_rating = Column(Float, nullable=False)
price_rating = Column(Float, nullable=False)
service_rating = Column(Float, nullable=False)
vibe_rating = Column(Float, nullable=False)


class RatingBase(BaseModel):
    user_id: int
    restaurant_id: int
    food_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    price_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    service_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0
    vibe_rating: confloat(ge=1.0, le=5.0)  # Float constrained between 1.0 and 5.0


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
