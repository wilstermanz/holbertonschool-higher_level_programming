#!/usr/bin/python3
"""Script to print all states containing letter a """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id, State.name)\
                   .filter(State.name.like(argv[4]))\
                   .first()
    if state:
        print(f"{state[0]}")
    else:
        print('Nothing')

    session.close()
