import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials for demonstration
    valid_username = "user123"
    valid_password = "pass123"

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def reset_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Login Application")
root.geometry("300x200")
root.resizable(False, False)

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Buttons
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=5)

# Run the application
root.mainloop()

# ACTIVITY DOES NOT RUN ON VSC, OPEN REPLIT > TKINTER TO RUN