import mysql.connector

# Define a connection variable

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school_management_sys"
)


# if conn.is_connected():
#     print("Database Connection Successful!")

'''
    Defining a cursor object to use it for executing queries all over this codeplace.
'''

cursor = conn.cursor()

'''
Create a database using SQL (Structured Query Language) which 
    is used to communicate with MySQL Databases.
'''

# cursor.execute("CREATE DATABASE school_management_sys")

'''
    Create a table for students' records where fields are 
    student id, full name, class, roll no., address, and date of birth.
'''

# cursor.execute("""
#     CREATE TABLE students (
#         student_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
#         full_name VARCHAR(100) NOT NULL,
#         class_name VARCHAR(50) NOT NULL,
#         roll_no INTEGER NOT NULL,
#         address TEXT,
#         date_of_birth DATE
#     )
# """)

'''
Inserting a few records in students table using INSERT Query.
'''

# sql = "INSERT INTO students (full_name, class_name, roll_no, address, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
# values = ("Sunita Hiski", "12", 5, "Tansen - 06, Palpa", "2059-08-12")

# cursor.execute(sql, values)
# conn.commit()

# sql = "INSERT INTO students (full_name, class_name, roll_no, address, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
# values = [
#     ("Sunita Hiski", "12", 5, "Tansen - 06, Palpa", "2059-08-12"),
#     ("Rubina Rana", "11", 10, "Tansen - 03, Palpa", "2059-08-12"),
#     ("Ritesh Pun", "12", 8, "Tansen - 04, Palpa", "2059-08-12"),
#     ("Bhumika Soti", "11", 9, "Tansen - 08, Palpa", "2059-08-12")
# ]

# cursor.executemany(sql, values)
# conn.commit()

'''
Fetching records from students table using SELECT Query.
'''

# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

'''
Conditional Fetch 
'''

cursor.execute("SELECT * FROM students WHERE class_name = '11'")
records = cursor.fetchall()
for record in records:
    print(record)