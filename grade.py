#Create a table 'students' with fields:id, name, age, grade. Write SQL and PYTHON code.

import mysql.connector

#Defining  a connection  variable

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_management_sys"
)
cursor = conn.cursor()

'''
Create a database using SQL(Structured Query Language) which is used to communicate with MYSQL Databases.
'''

# cursor.execute("CREATE DATABASE student_management_sys")

'''
Create a table for students records where fields are student id, name, age, and grade.
'''
# cursor.execute("""
# CREATE TABLE students(
#     student_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     name VARCHAR(100) NOT NULL,
#     age INTEGER NOT NULL,
#     grade VARCHAR(100) NOT NULL
# )
# """)


# '''
# Inserting a few records in students table using INSERT Query
# '''
# sql = "INSERT INTO students(name, age, grade) VALUES(%s, %s, %s)"
# values = ("John Thapa", "22", "12")


# cursor.execute(sql, values)
# conn.commit()

# sql = "INSERT INTO students(name, age, grade) VALUES(%s, %s, %s)"
# values = [
#     ("John Thapa", "22", "12"),
#     ("Rosy Magar", "20", "10"),
#     ("Bhumika Thapa", "18", "9"),
# ]

# cursor.executemany(sql, values)
# conn.commit()






