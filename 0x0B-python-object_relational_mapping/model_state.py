#!/usr/bin/python3
"""
Contains class definition of a state and an
instance of Base = declatative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )
    name = Column(String(128), nullable=False)
