#!/usr/bin/python3
"""deletes all State objects with a name containing letter a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    deleted_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in deleted_states:
        session.delete(state)
    session.commit()

    session.close()
