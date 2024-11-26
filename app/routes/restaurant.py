from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db.db_connection import DatabaseConnection
from app.crud.restaurant import get_restaurants
from app.schemas.restaurant import Restaurant

router = APIRouter()


@router.get("/", response_model=list[Restaurant])
def get_restaurants_route(skip: int = 0, limit: int = None, db: Session = Depends(DatabaseConnection.get_db)):
    """
    Get a list of all restaurants.
    Supports pagination using `skip` and `limit`.
    """
    restaurants = get_restaurants(db, skip=skip, limit=limit)
    return restaurants
