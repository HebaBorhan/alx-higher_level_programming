#!/usr/bin/python3
"""Creates the State California with the City San Francisco"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_tables(engine):
    """Create tables if they do not exist"""
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    session.add(california)
    session.add(san_francisco)

    session.commit()

    session.close()
