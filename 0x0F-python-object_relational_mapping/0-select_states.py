#!/usr/bin/python3
"""Python3 Script"""

import sys
import MySQLdb


def list_states(username, password, database):
    """Connect to MySQL server"""
    try:
        connection = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = connection.cursor()

        # Execute query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display states
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close connection
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
