import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        name = name_entry.get()
        dob_day = int(day_entry.get())
        dob_month = int(month_entry.get())
        dob_year = int(year_entry.get())
        dob = datetime(dob_year, dob_month, dob_day)
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if not name.strip():
            name = "User"  # Default name if left blank
        messagebox.showinfo("Age", f"Hey {name}! Your age is {age} years.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid information.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(root, text="Welcome to the Age Calculator", font=("Helvetica", 16), bg="#f0f8ff", fg="#333")
title_label.pack(pady=10)

# Name Field
tk.Label(root, text="Your Name:", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=5)
name_entry = tk.Entry(root, font=("Helvetica", 12), width=25)
name_entry.pack(pady=5)

# Date of Birth Fields
tk.Label(root, text="Date of Birth (DD/MM/YYYY):", font=("Helvetica", 12), bg="#f0f8ff").pack(pady=10)
dob_frame = tk.Frame(root, bg="#f0f8ff")
dob_frame.pack(pady=5)
day_entry = tk.Entry(dob_frame, font=("Helvetica", 12), width=5)
day_entry.pack(side="left", padx=5)
tk.Label(dob_frame, text="/", font=("Helvetica", 12), bg="#f0f8ff").pack(side="left")
month_entry = tk.Entry(dob_frame, font=("Helvetica", 12), width=5)
month_entry.pack(side="left", padx=5)
tk.Label(dob_frame, text="/", font=("Helvetica", 12), bg="#f0f8ff").pack(side="left")
year_entry = tk.Entry(dob_frame, font=("Helvetica", 12), width=8)
year_entry.pack(side="left", padx=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Age", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=calculate_age)
calculate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

  # ACTIVITY DOES NOT RUN ON VSC, OPEN REPLIT > TKINTER TO RUN