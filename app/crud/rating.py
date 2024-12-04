from app.dependencies.db.models.rating import Rating
from sqlalchemy.orm import Session


def delete_ratings_by_restaurant_id(db: Session, user_id: int, restaurant_id: int):
    try:
        # Delete ratings matching both user_id and restaurant_id
        db.query(Rating).filter(Rating.user_id == user_id, Rating.restaurant_id == restaurant_id).delete(
            synchronize_session=False)
        db.commit()
        return {"message": "Ratings deleted successfully"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
