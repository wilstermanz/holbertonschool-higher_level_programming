#!/usr/bin/python3
"""
Contains class definition of a city and an
instance of Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
