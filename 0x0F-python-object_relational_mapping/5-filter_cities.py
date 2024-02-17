#!/usr/bin/python3
"""A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> "
              "<password> <database> <state_name>")
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cursor = db.cursor()

        # Prepare SQL query with parameterized input to avoid SQL injection
        query = """SELECT cities.id, cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"""

        # Execute SQL query with parameterized input
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
