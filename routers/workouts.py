from fastapi import Body, Depends, FastAPI, HTTPException, Response, status, APIRouter
from .. import models, schemas, utils, oauth
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db

router = APIRouter()


@router.get('/sqlalchemy')
def test(db: Session = Depends(get_db), user_id: int = Depends(oauth.get_current_user)):
    users = db.query(models.Users).all()
    print(user_id)
    return {"data": users}


@router.get('/history', )
def root(db: Session = Depends(get_db)):
    data = db.query(models.Streaks).all()

    return {"data": data}
