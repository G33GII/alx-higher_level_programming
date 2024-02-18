#!/usr/bin/python3
"""Python SQLalchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username, password, database = sys.argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close session
    session.close()
