#!/usr/bin/python3
"""Pythone SQL code"""

import sys
import MySQLdb


def list_states_starting_with_n(username, password, database):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = connection.cursor()

        # Execute query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states "
                       "WHERE name LIKE 'N%' ORDER BY id ASC")
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

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_starting_with_n(username, password, database)
