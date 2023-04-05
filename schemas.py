import datetime
from pydantic import BaseModel, EmailStr


class Workout_history(BaseModel):
    workout_name: str
    time: int
    sets: int


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
