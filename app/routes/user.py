from app.dependencies.db.db_connection import DatabaseConnection
from fastapi import APIRouter, HTTPException, Depends
from app.crud.user import create_user, get_user
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/add_user", status_code=201)
def add_user(user: UserCreate, db: Session = Depends(DatabaseConnection.get_db)):
    # Check if the user already exists
    existing_user = get_user(db, user.email)
    if existing_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new user object
    new_user = create_user(db, user.username, user.email)

    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}
