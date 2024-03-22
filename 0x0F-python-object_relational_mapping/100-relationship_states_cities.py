#!/usr/bin/python3
"""Script to create the State "California"
with the City "San Francisco" from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_and_city(username, password, db_name):
    """Create the State "California" with the City "San Francisco""""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.add(san_francisco)
    session.commit()


if __name__ == "__main__":

    username, password, db_name = sys.argv[1:]
    create_state_and_city(username, password, db_name)
