import tkinter as tk
import mysql.connector

main_window = tk.Tk()
main_window.geometry("400x400")
main_window.title("My First Application")

# Defining a function to get the inputs

# A function to connect app with database
def db_connect():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "authentication"
    )

    return conn

connect = db_connect()

if connect.is_connected():
    print("Database Connection Successful!")

cursor = connect.cursor()
# Defining a function to create a database
def create_db():
    cursor.execute("CREATE DATABASE authentication")

# Calling the fucntion to create database
#create_db()

# Defining a function to create a table named users
def create_users_table():
    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            confirm_pwd VARCHAR(255) NOT NULL
        )
    """)

# Calling the function to create table
#create_users_table()

# A function to insert data into database
def insert_user(username, password, confirm_pwd):
    sql = "INSERT INTO `users`(`username`, `password`, `confirm_pwd`) VALUES (%s, %s, %s)"
    value = (username, password, confirm_pwd)
    cursor.execute(sql,value)
    connect.commit()

def get_inputs():
    username = user_entry.get()
    password = pwd_entry.get()
    confirm_password = con_entry.get()

    # Validating the user password and confirm password whether they match or not
    if password != confirm_password:
        msg = tk.Label(main_window, text=f"Passwords do not match!", fg="#ff0000")
        msg.pack()
    else:
        # Calling the function to insert user's info to the database
        insert_user(username, password, confirm_password)
        msg = tk.Label(main_window, text=f"Data stored successfully!", fg="#00ff00")
        msg.pack()
    
    # Displaying the fetched data in the console
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Confirm Password: {confirm_password}")
     
    # Displaying the fetched data in the screen of app
    res_label1 = tk.Label(main_window, text=f"Username: {username}")
    res_label1.pack()

    res_label2 = tk.Label(main_window, text=f"Password: {password}")
    res_label2.pack()

    res_label3 = tk.Label(main_window, text=f"Confirm Password: {confirm_password}")
    res_label3.pack()

# Defining widgets
user_label = tk.Label(main_window, text="Username", font=("Algerian", 20, "bold"), fg="#ff4500")
user_label.pack(padx=10, pady=10)

user_entry = tk.Entry(main_window)
user_entry.pack()

pwd_label = tk.Label(main_window, text="Password")
pwd_label.pack(padx=10, pady=10)

pwd_entry = tk.Entry(main_window)
pwd_entry.pack()

con_label = tk.Label(main_window, text="Confirm Password")
con_label.pack(padx=10,pady=10)

con_entry = tk.Entry(main_window)
con_entry.pack()

signup_btn = tk.Button(main_window, text="Sign Up", fg="#ff4500", command=get_inputs)
signup_btn.pack(padx=10,pady=10)

main_window.mainloop()