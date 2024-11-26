from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    formatted_address: str
    lat: float
    lng: float
    icon: str


class RestaurantCreate(RestaurantBase):
    pass


class Restaurant(RestaurantBase):
    id: int

    class Config:
        orm_mode = True
