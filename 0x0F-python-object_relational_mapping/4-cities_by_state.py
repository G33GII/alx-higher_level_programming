#!/usr/bin/python3
"""
Lists all cities with their corresponding states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SQL query to retrieve cities and their corresponding states
        cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                        cities INNER JOIN states ON states.id=cities.state_id""")

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
