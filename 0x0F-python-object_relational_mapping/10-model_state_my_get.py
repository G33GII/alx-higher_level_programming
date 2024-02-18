#!/usr/bin/python3
"""Python SQLalchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query the State object with the provided name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if state is found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
