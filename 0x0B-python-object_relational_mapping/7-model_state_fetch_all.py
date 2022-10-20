#!/usr/bin/python3
"""Script to list State Objects"""

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

    for state in session.query(State.id, State.name)\
                        .order_by(State.id.asc())\
                        .all():
        print("{}: {}".format(state.id, state.name))

    session.close()
