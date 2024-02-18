#!/usr/bin/python3
"""Python SQLalchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extract MySQL connection information from command-line arguments
    username, password, database = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query and list all State objects containing the letter 'a'
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
