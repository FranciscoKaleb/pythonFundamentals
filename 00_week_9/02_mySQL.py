

# same thing as before but using with statements to ensure proper resource management

import mysql.connector

config = {
    "host": "localhost",
    "user": "franciscokaleb",
    "password": "1234567&",
    "database": "user_db"
}

# using with ensures that the connection and cursor are properly closed even if an error occurs
with mysql.connector.connect(**config) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM cashiers")
        cursor = cursor.fetchall() # rows is a list of tuples, each tuple represents a row in the users table

for row in cursor:
    print(row)


