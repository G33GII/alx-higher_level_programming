#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa for a given state.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    db_connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object to execute SQL queries
    db_cursor = db_connection.cursor()

    # Define the SQL query to retrieve cities for the given state
    sql_query = """SELECT cities.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s"""

    # Execute the SQL query with parameterized input for the state name
    state_name = sys.argv[4]
    db_cursor.execute(sql_query, (state_name,))

    # Fetch all rows from the result set
    rows = db_cursor.fetchall()

    # Extract city names from fetched rows and create a list
    city_names = [row[0] for row in rows]

    # Print the city names separated by commas
    print(*city_names, sep=", ")

    # Close cursor and database connection
    db_cursor.close()
    db_connection.close()
