#!/usr/bin/python3
"""Script to list all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities_by_state(username, password, db_name):
    """List all City objects from the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:]
    list_cities_by_state(username, password, db_name)
