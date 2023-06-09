from fastapi import Body, Depends, FastAPI, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from .. import database, schemas, models, utils, oauth
router = APIRouter(tags=['Authentication'])


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.Users).filter(
        models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    access_token = oauth.create_token(data={"user_id": user.id})

    return {"access": access_token, "token_type": "bearer"}
