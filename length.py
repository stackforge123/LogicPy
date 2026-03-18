import tkinter as tk
import mysql.connector

main_window = tk.Tk()
main_window.geometry("400x400")
main_window.title("Rectangle Area Calculator")


def calculate_area():
    length = float(length_Entry.get())
    breadth = float(breadth_Entry.get())
    area = length*breadth

    result = tk.Label (text = f"Area: {area}")
    result.grid()

# Defining widgets

length_Label = tk.Label (main_window, text="length",)
length_Label.grid (row=0, column=0, )

length_Entry = tk.Entry(main_window)
length_Entry.grid(row=0, column=1, )

breadth_Label = tk.Label (main_window, text="breadth",)
breadth_Label.grid(row=1, column=0, )

breadth_Entry = tk.Entry(main_window)
breadth_Entry.grid(row=1, column=1 )

calculate_btn = tk.Button (main_window, text="calculate Area", command=calculate_area)
calculate_btn.grid(row=2,column=1, columnspan=3)

main_window.mainloop()