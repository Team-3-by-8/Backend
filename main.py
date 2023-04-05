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


@ app.get('/')
async def root():

    return {"message": "hello worlddffdf"}


@ app.get('/sqlalchemy')
def test(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return {"data": users}


@ app.get('/history')
def root():
    cursor.execute("""SELECT * FROM workout_history""")
    data = cursor.fetchall()
    print(data)
    return {"data": data}


@ app.post("/createworkout",)
def createuser(workouts: Workout_history):

    cursor.execute("""INSERT INTO workout_history(workout_name,time,sets) VALUES(%s,%s,%s) RETURNING * """,
                   (workouts.workout_name, workouts.time, workouts.sets))
    new_workout = cursor.fetchone()
    conn.commit()

    return {"data": new_workout}


# @app.get('/history/{id}')
# def root(id: int):
#     cursor.execute(
#         """SELECT * FROM workout_history WHERE id = %s""", (str(id)))
#     data = cursor.fetchall()
#     print(data)
#     return {"data": data}


@app.get('/history/{workout_name}')
def workout_search(workout_name):
    cursor.execute(
        """SELECT * FROM workout_history WHERE workout_name = %s""", (workout_name,))
    data = cursor.fetchall()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found")
    return {"data": data}


@app.delete('/history/{id}')
def updateworkout(id: int):
    cursor.execute(
        """DELETE FROM workout_history WHERE id = %s RETURNING *""", (str(id),))
    data = cursor.fetchone()
    conn.commit()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found or already deleted")
    return {"data": data}


@app.put('/history/{id}')
def updateworkout(id: int, data: Workout_history):
    cursor.execute(
        """UPDATE workout_history SET workout_name = %s, time = %s, sets = %s WHERE id = %s RETURNING *""",
        (data.workout_name, data.time, data.sets, str(id)))

    updated_data = cursor.fetchone()
    conn.commit()
    if not updated_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found")
    return {"data": updated_data}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    # user.password = hashed_password
    # new_user = models.Users(**user.dict())  # {'email' : 'JohnDoe', 'password' : 'aaaabbb'}
    new_user = models.Users(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
