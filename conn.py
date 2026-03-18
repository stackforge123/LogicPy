import mysql.connector

#Defining a connection variable.

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school_management_sys"
)

# if conn.is_connected():
#     print("Database Connection Successful!")

cur = conn.cursor()
cur.execute("CREATE DATABASE system_database")


