from app.models.types import Restaurant, User
from typing import List


class DBHandler:

    users: List[User] = []
    restaurants: List[Restaurant] = [
        Restaurant(**{"id": 1, "name": "Pizza Place", "location": "New York"}),
        Restaurant(**{"id": 2, "name": "Sushi World", "location": "San Francisco"}),
        Restaurant(**{"id": 3, "name": "Burger King", "location": "Los Angeles"}),
    ]

    @staticmethod
    def get_favorites_restaurants(user_id: str) -> List[Restaurant]:
        return [
            Restaurant(**{"id": 1, "name": "Pizza Place", "location": "New York"})
        ]

    @staticmethod
    def get_all_restaurants() -> List[Restaurant]:
        return DBHandler.restaurants

    @staticmethod
    def add_user(user: User):
        DBHandler.users.append(user)
