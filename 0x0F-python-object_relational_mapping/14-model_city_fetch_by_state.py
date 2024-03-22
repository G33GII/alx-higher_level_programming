#!/usr/bin/python3
"""Script to fetch and print all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """Fetch and print all City objects from the database"""

    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # ct = session.query(State.name, City.id, City.name).filter(State.id == City.state_id)
    for instance in ct:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
