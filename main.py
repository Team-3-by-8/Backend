from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .import models
from .database import engine
from .routers import workouts, users, auth
from dotenv import load_dotenv
import os

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
USER = os.getenv('DBUSERNAME')
PASSWORD = os.getenv('PASSWORD')
ADDRESS = os.getenv('ADDRESS')
DATABASE_NAME = os.getenv('DATABASE_NAME')

while True:
    try:
        conn = psycopg2.connect(host=ADDRESS, database=DATABASE_NAME,
                                user=USER, password=PASSWORD, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Running Workout Diary Database')
        break
    except Exception as error:
        print('Error running Workout Diary Database')
        print('Error running Workout Diary Database: ', error)
        time.sleep(3)

app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(auth.router)


@ app.get('/')
async def root():
    return {"message": "hello world"}
