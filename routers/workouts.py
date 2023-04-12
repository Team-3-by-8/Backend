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


# @router.post("/createworkout",)
# def createuser(workouts: Workout_history):

#     cursor.execute("""INSERT INTO workout_history(workout_name,time,sets) VALUES(%s,%s,%s) RETURNING * """,
#                    (workouts.workout_name, workouts.time, workouts.sets))
#     new_workout = cursor.fetchone()
#     conn.commit()

#     return {"data": new_workout}


# # @router.get('/history/{id}')
# # def root(id: int):
# #     cursor.execute(
# #         """SELECT * FROM workout_history WHERE id = %s""", (str(id)))
# #     data = cursor.fetchall()
# #     print(data)
# #     return {"data": data}


# @router.get('/history/{workout_name}')
# def workout_search(workout_name):
#     cursor.execute(
#         """SELECT * FROM workout_history WHERE workout_name = %s""", (workout_name,))
#     data = cursor.fetchall()
#     if not data:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found")
#     return {"data": data}


# @router.delete('/history/{id}')
# def updateworkout(id: int):
#     cursor.execute(
#         """DELETE FROM workout_history WHERE id = %s RETURNING *""", (str(id),))
#     data = cursor.fetchone()
#     conn.commit()
#     if not data:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found or already deleted")
#     return {"data": data}


# @router.put('/history/{id}')
# def updateworkout(id: int, data: Workout_history):
#     cursor.execute(
#         """UPDATE workout_history SET workout_name = %s, time = %s, sets = %s WHERE id = %s RETURNING *""",
#         (data.workout_name, data.time, data.sets, str(id)))

#     updated_data = cursor.fetchone()
#     conn.commit()
#     if not updated_data:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found")
#     return {"data": updated_data}
