from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    creation_date = Column(TIMESTAMP(timezone=True),
                           nullable=False, server_default=text('now()'))


class Streaks(Base):
    __tablename__ = 'streaks'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    streak = Column(Integer, nullable=True,)
    freezes = Column(Integer, nullable=True)
    freeze_refill_in = Column(Integer, nullable=True)


class Types(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=True,)
    isListed = Column(Boolean, nullable=True)


class Weeklyplan(Base):
    __tablename__ = 'weekly_plan'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=True,)
    duration = Column(Integer, nullable=True)

    type = relationship('Types', backref='weekly_plan')


class Activities(Base):
    __tablename__ = 'actvities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    date = Column(Integer, nullable=True,)
    duration = Column(Integer, nullable=True)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=True,)
    max_HR = Column(Integer, nullable=True)
    min_HR = Column(Integer, nullable=True)
    average_HR = Column(Integer, nullable=True)

    type = relationship('Types', backref='activities')
