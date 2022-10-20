#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""

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

    session.add(State(name='Louisiana'))
    louisiana = session.query(State).filter_by(name='Louisiana')\
                       .order_by(State.id.desc())\
                       .first()
    session.commit()
    print(louisiana.id)

    session.close()
