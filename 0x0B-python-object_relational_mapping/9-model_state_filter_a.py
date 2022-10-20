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

    for a_state in session.query(State.id, State.name)\
                          .order_by(State.id.asc())\
                          .filter(State.name.like('%a%')):
        print(f"{a_state.id}: {a_state.name}")

    session.close()
