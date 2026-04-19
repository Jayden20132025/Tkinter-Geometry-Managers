# Import tkinter
import tkinter as tk

# Import datetime
from datetime import datetime

# Create window
window = tk.Tk()
window.title("Age Calculator App")
window.geometry("400x400")
window.config(bg="#E3F2FD")


# Function to calculate age
def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = datetime.today()

        age = today.year - year

        # Check birthday
        if (today.month, today.day) < (month, day):
            age -= 1

        result_label.config(
            text=f"Hello {name}! You are {age} years old 🎉",
            fg="darkblue"
        )

    except:
        result_label.config(
            text="Please enter valid numbers!",
            fg="red"
        )


# Heading
heading = tk.Label(
    window,
    text="Age Calculator",
    font=("Arial", 16, "bold"),
    bg="#E3F2FD"
)
heading.grid(row=0, column=0, columnspan=2, pady=10)


# Name
tk.Label(window, text="Name:", bg="#E3F2FD").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)


# Day
tk.Label(window, text="Day:", bg="#E3F2FD").grid(row=2, column=0, padx=10, pady=5)
day_entry = tk.Entry(window)
day_entry.grid(row=2, column=1)


# Month
tk.Label(window, text="Month:", bg="#E3F2FD").grid(row=3, column=0, padx=10, pady=5)
month_entry = tk.Entry(window)
month_entry.grid(row=3, column=1)


# Year
tk.Label(window, text="Year:", bg="#E3F2FD").grid(row=4, column=0, padx=10, pady=5)
year_entry = tk.Entry(window)
year_entry.grid(row=4, column=1)


# Button
tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age,
    bg="#4CAF50",
    fg="white"
).grid(row=5, column=0, columnspan=2, pady=15)


# Result
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#E3F2FD")
result_label.grid(row=6, column=0, columnspan=2, pady=10)


window.mainloop()