import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session as SQLAlchemySession


# Singleton pattern for database connection and session
class DatabaseConnection:
    _engine = None
    _SessionLocal = None

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            DATABASE_URL = os.getenv("DATABASE_URL")  # Get the database URL from environment variable
            if DATABASE_URL is None:
                raise ConnectionError("DATABASE_URL environment variable does not exists")
            # Create the engine for the first time if it does not exist
            cls._engine = create_engine(DATABASE_URL, echo=True)
        return cls._engine

    @classmethod
    def get_session(cls) -> SQLAlchemySession:
        if cls._SessionLocal is None:
            # Create session factory the first time
            cls._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.get_engine())
        return cls._SessionLocal()

    @classmethod
    def get_db(cls):
        db = cls.get_session()
        try:
            yield db
        finally:
            db.close()
