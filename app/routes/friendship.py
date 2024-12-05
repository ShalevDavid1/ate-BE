from app.crud.friendship import get_friends, add_friendship, get_friendship
from app.dependencies.db.db_connection import DatabaseConnection
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.user import get_user
from app.schemas.user import User

router = APIRouter()


@router.get("/")
def get_friends_route(email: str, db: Session = Depends(DatabaseConnection.get_db)):
    """
    Gets user email and returns his friends emails.
    """
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=400, detail="Email is not registered")

    friends = get_friends(db, user.id)
    return [{"id": f.id, "email": f.email, "username": f.username} for f in friends]


@router.post("/add_friendship", response_model=User)
def add_friendship_route(email: str, friend_email: str,
                         db: Session = Depends(DatabaseConnection.get_db)):
    """
    Gets email: str and friend_email: str Inserts as row to the DB
    Ands returns friend information
    """

    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=400, detail="User email is not registered")

    friend = get_user(db, friend_email)
    if friend is None:
        raise HTTPException(status_code=400, detail="Friend email is not registered")

    user_id = user.id
    friend_id = friend.id

    if user_id == friend_id:
        raise HTTPException(status_code=400, detail="A user cannot be friends with themselves.")

    friendship = get_friendship(db, user_id, friend_id)
    if friendship is not None:
        raise HTTPException(status_code=400, detail="Friendship already exists")

    friendship_added = add_friendship(db, user_id, friend_id)
    if "error" in friendship_added:
        raise HTTPException(status_code=400, detail=friendship_added["error"])

    return friend
