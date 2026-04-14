

# same thing as before but using with statements to ensure proper resource management

import mysql.connector

config = {
    "host": "localhost",
    "user": "franciscokaleb",
    "password": "1234567&",
    "database": "user_db"
}

# using with ensures that the connection and cursor are properly closed even if an error occurs
# if connection are not closed, it can lead to resource leaks and eventually exhaust the database connection pool
# its running in the background and consuming resources, even if the main program has finished executing
with mysql.connector.connect(**config) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        cursor = cursor.fetchall() # rows is a list of tuples, each tuple represents a row in the users table

for row in cursor:
    print(row)


