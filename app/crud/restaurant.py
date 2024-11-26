from sqlalchemy.orm import Session
from app.dependencies.db.models.restaurant import Restaurant


def get_restaurants(db: Session, skip: int = 0, limit: int = None):
    # Query the database and return the list of restaurants
    query = db.query(Restaurant)
    query = query.offset(skip)
    if limit is not None:
        query = query.limit(limit)
    return query.all()
