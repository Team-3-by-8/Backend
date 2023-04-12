from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .import models
from .database import engine
from .routers import workouts, users, auth


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
app.include_router(auth.router)


@ app.get('/')
async def root():

    return {"message": "hello worlddffdf"}
