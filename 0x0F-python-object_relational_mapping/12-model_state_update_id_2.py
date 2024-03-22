#!/usr/bin/python3
"""Script to change the name of a State object in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, db_name):
    """Change the name of the State where id = 2 to New Mexico"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()
    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()

if __name__ == "__main__":=
    username, password, db_name = sys.argv[1:]
    change_state_name(username, password, db_name)
