import tkinter as tk
import mysql.connector

main_window = tk.Tk()
main_window.geometry("300x400")
main_window.title("Simple Interest Calculator")

def calculate_interest():
    Principal = float(principal_Entry.get())
    Time = float(time_Entry.get())
    Rate = float(rate_Entry.get())
    Simple_Interest = (Principal * Time * Rate)

    result = tk.Label (text = f"Interest: {Simple_Interest}")
    result.grid()

# Defining widgets

principal_Label = tk.Label(main_window, text="principal",)
principal_Label.grid(row=0, column=1)

principal_Entry = tk.Entry(main_window)
principal_Entry.grid(row=0,column=2)

rate_Label = tk.Label(main_window, text="rate",)
rate_Label.grid(row=1,column=1)

rate_Entry = tk.Entry(main_window)
rate_Entry.grid(row=1,column=2)

time_Label = tk.Label(main_window, text="time",)
time_Label.grid(row=2, column=1)

time_Entry = tk.Entry(main_window)
time_Entry.grid(row=2, column=2)

calculate_btn = tk.Button(main_window, text="calculate Interest", command=calculate_interest)
calculate_btn.grid(row=3,column=1, columnspan=3)

main_window.mainloop()