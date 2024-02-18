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

    # Query and print the first State object
    first_state = session.query(State).first()

    # Check if a state is found
    if first_state:
        print(first_state.id, first_state.name, sep=": ")
    else:
        print("Nothing")

    # Close session
    session.close()
