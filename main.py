from http import HTTPStatus

from fastapi import Body, Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session

from .import models, schemas, utils
from .schemas import Workout_history
from .database import get_db, engine, SessionLocal
from .routers import workouts, users


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='workoutdiary',
                                user='postgres', password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Running workout history')
        break
    except Exception as error:
        print('Error running workout history')
        print('Error running workout history: ', error)
        time.sleep(3)

app.include_router(users.router)
app.include_router(workouts.router)


@ app.get('/')
async def root():

    return {"message": "hello worlddffdf"}
