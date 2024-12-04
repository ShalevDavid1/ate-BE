from app.crud.rating import delete_ratings_by_restaurant_id
from app.crud.restaurant import get_restaurants
from app.dependencies.db.db_connection import DatabaseConnection
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.user import get_user

router = APIRouter()


@router.delete("/delete_rated_restaurant")
def delete_rated_restaurant(email: str, restaurant_id: int,
                            db: Session = Depends(DatabaseConnection.get_db)):
    """
    Deletes ratings of restaurants, and keeps the restaurant data.
    """
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=400, detail="Email is not registered")

    return delete_ratings_by_restaurant_id(db, user.id, restaurant_id)
