from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


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


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
