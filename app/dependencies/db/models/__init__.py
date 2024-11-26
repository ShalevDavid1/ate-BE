from sqlalchemy.ext.declarative import declarative_base

# Define the base for our schemas
Base = declarative_base()

USERS_TABLE_NAME = "users"
RESTAURANTS_TABLE_NAME = "restaurants"
RATINGS_TABLE_NAME = "ratings"
FRIENDSHIPS_TABLE_NAME = "friendships"

if __name__ == "__main__":
    # Create tables if they don't exist
    from app.dependencies.db.db_connection import DatabaseConnection

    Base.metadata.create_all(bind=DatabaseConnection.get_engine())

    # Using the singleton session to interact with the database
    # db = DatabaseConnection.get_db()  # Get the singleton session
    db = next(DatabaseConnection.get_db())  # Get the singleton session
