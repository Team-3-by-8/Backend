from pydantic import BaseModel, EmailStr
from datetime import datetime


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
    creation_date: datetime

    class Config:
        orm_mode = True
