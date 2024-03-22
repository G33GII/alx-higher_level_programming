#!/usr/bin/python3
"""Script to delete State objects with a name containing the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_a(username, password, db_name):
    """Delete State objects with a name containing the letter 'a'"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    delete_states_with_a(username, password, db_name)
