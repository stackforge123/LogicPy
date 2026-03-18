    # Objective: Create a tkinter GUI that acts a user registration system.

import tkinter as tk
import mysql.connector
from tkinter import messagebox  

main_window = tk.Tk()
main_window.geometry("500x500")
main_window.title("Registration Window")

    # A function to validate user inputs

def validate_registration():
        Full_Name = Full_Name_Entry.get()
        Username = Username_Entry.get()
        Email = Email_Entry.get()
        Password = Password_Entry.get()

        if Full_Name=="" or Username=="" or Email=="" or Password=="":
            messagebox.showerror("Error", "All fields are required.")

        if len(Password) < 8:
            messagebox.showerror("Error", "password must be of 8 characters.")

        print(f"Full_Name: {Full_Name}")
        print(f"Username: {Username}")
        print(f"Email: {Email}")
        print(f"Password: {Password}")
        messagebox.showinfo("Success", "Registration Successed!")

def clear_fields():
        Full_Name_Entry.delete(0, tk.END)
        Username_Entry.delete(0, tk. END)
        Email_Entry.delete(0, tk.END)
        Password_Entry.delete(0, tk.END)

    # Defining a widgets
Full_Name_Label = tk.Label(main_window, text= "Full Name: ", font=("Arial", 16, "bold"), fg="red")
Full_Name_Label.grid(row=0, column=1)

Full_Name_Entry = tk.Entry(main_window)
Full_Name_Entry.grid(row=0, column=2)

Username_Label = tk.Label(main_window, text="Username:", font=("Arial", 16, "bold"), fg="red")
Username_Label.grid(row=1, column=1)

Username_Entry = tk.Entry(main_window)
Username_Entry.grid(row=1, column=2)

Email_Label = tk.Label(main_window, text="Email:", font=("Arial", 16, "bold"), fg="red")
Email_Label.grid(row=2, column=1)

Email_Entry = tk.Entry(main_window)
Email_Entry.grid(row=2, column=2)

Password_Label = tk.Label(main_window, text="Password:", font=("Arial", 16, "bold"), fg="red")
Password_Label.grid(row=3,column=1)

    
Password_Entry = tk.Entry(main_window, show="*")
Password_Entry.grid(row=3, column=2)

Submit_btn = tk.Button(main_window, text="Submit", command=validate_registration)
Submit_btn.place(relx=0.3,rely=0.3)

Clear_btn = tk.Button(main_window, text="Clear", command=clear_fields)
Clear_btn.place(relx=0.5,rely=0.3)


main_window.mainloop()