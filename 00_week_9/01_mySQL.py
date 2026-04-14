

# install mySQL connector first
# pip install mysql-connector-python

import mysql.connector

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="franciscokaleb",
    password="1234567&",
    database="user_db"
)

cursor = conn.cursor()

# 2. Execute a sample SELECT query
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall() # rows is a list of tuples, each tuple represents a row in the users table

for row in rows:
    print(row)

# 3. Close the connection
cursor.close()
conn.close()








