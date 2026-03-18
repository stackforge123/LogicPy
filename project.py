import mysql.connector

#Define a connection variable 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_management_sys"
)


#if conn.is_conected():
# print("Database connection Successful!")

'''
   Defining a cursor object to use it for executing queries all over this codeplace.
'''
cursor = conn.cursor()

'''
Create a database using SQL(Structured Query Language) which  is used to communicate wuth MYSQL Databases.
'''

# cursor.execute("CREATE DATABASE employee_management_sys")

'''
   Create a table for students records where fields are
    Student id, full name, class, roll no., address, and date of birth.
'''

# cursor.execute("""
# CREATE TABLE employees(
#      employee_id iNTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
#      full_name VARCHAR(100) NOT NULL, 
#      post_name VARCHAR(100) NOT NULL,
#      salary DOUBLE(12,2) NOT NULL,
#      address TEXT,
#      date_of_birth DATE
# )               
# """)

'''
Inserting a few records in employee table using INSERT Query.
'''

sql="INSERT INTO employees (full_name, post_name, salary, address, date_of_birth) VALUES(%s, %s, %s, %s,%s)"
values = [
    ("John Thapa", "Manager", "30000", "Butwal-09, Sukhanagar", "2055-10-4"),
    ("Hem Gharti", "DSP", "50000", "Tansen-08, Palpa", "2051-3-6"),
    ("Miruna Magar", "Supervisior", "45000", "Butwal-01 Ramnagar", "2057-11-9"),
]
cursor.executemany(sql, values)
conn.commit()

'''
Fetching records from students table using SELECT Query.
'''

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

'''
Conditional Fetch  
'''

cursor.execute("SELECT * FROM employees WHERE post_name ='Manager'")
records = cursor.fetchall()
for record in records:
    print(record)
    



