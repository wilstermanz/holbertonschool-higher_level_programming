#!/usr/bin/python3
"""Script to print the first State object """

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

    states = session.query(State.id, State.name)\
                    .order_by(State.id.asc())\
                    .all()
    print("{}: {}".format(states[0][0], states[0][1]))

    session.close()
