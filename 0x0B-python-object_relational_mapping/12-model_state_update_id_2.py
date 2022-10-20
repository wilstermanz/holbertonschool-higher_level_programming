#!/usr/bin/python3
"""changes the name of a State object from the database """

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

    to_change = session.query(State).filter_by(id=2).one()
    to_change.name = "New Mexico"

    session.commit()
    session.close()
