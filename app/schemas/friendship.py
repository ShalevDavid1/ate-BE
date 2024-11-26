from pydantic import BaseModel


class FriendshipBase(BaseModel):
    user_id: int
    friend_id: int


class FriendshipCreate(FriendshipBase):
    pass


class Friendship(FriendshipBase):
    id: int

    class Config:
        orm_mode = True
