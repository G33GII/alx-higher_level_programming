#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def list_cities(username, password, database):
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

        # Execute query to retrieve cities
        query = "SELECT cities.id, cities.name, states.name FROM "
        "cities INNER JOIN states ON states.id=cities.state_id"
        cursor.execute(query)
        cities = cursor.fetchall()

        # Display cities
        for city in cities:
            print(city)

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

    list_cities(username, password, database)
