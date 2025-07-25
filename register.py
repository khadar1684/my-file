import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def register_ticket():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    source = source_var.get()
    destination = dest_var.get()
    date = date_entry.get()

    if not name or not age or not date:
        messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    ticket_info = (
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender}\n"
        f"From: {source}\n"
        f"To: {destination}\n"
        f"Date: {date}"
    )

    messagebox.showinfo("Ticket Registered", f"Ticket successfully registered:\n\n{ticket_info}")

# GUI setup
root = tk.Tk()
root.title("Train Ticket Registration")
root.geometry("400x400")
root.configure(bg="#e0f7fa")

title = tk.Label(root, text="Train Ticket Registration", font=("Arial", 16, "bold"), bg="#e0f7fa")
title.pack(pady=10)

# Frame for form
form = tk.Frame(root, bg="#e0f7fa")
form.pack(pady=10)

# Name
tk.Label(form, text="Passenger Name:", bg="#e0f7fa").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form, width=30)
name_entry.grid(row=0, column=1)

# Age
tk.Label(form, text="Age:", bg="#e0f7fa").grid(row=1, column=0, sticky="w", pady=5)
age_entry = tk.Entry(form, width=30)
age_entry.grid(row=1, column=1)

# Gender
tk.Label(form, text="Gender:", bg="#e0f7fa").grid(row=2, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(form, textvariable=gender_var, values=["Male", "Female", "Other"], state="readonly", width=28)
gender_dropdown.grid(row=2, column=1)
gender_dropdown.current(0)

# Source
tk.Label(form, text="From:", bg="#e0f7fa").grid(row=3, column=0, sticky="w", pady=5)
source_var = tk.StringVar()
source_dropdown = ttk.Combobox(form, textvariable=source_var, values=["select","guntur", "vijayawada", "narasaraopeta","amaravati"], state="readonly", width=28)
source_dropdown.grid(row=3, column=1)
source_dropdown.current(0)

# Destination
tk.Label(form, text="To:", bg="#e0f7fa").grid(row=4, column=0, sticky="w", pady=5)
dest_var = tk.StringVar()
dest_dropdown = ttk.Combobox(form, textvariable=dest_var, values=["select","bellamkonda", "vinukonda", "hydarabad","mumbai"], state="readonly", width=28)
dest_dropdown.grid(row=4, column=1)
dest_dropdown.current(0)

# Travel Date
tk.Label(form, text="Travel Date (DD-MM-YYYY):", bg="#e0f7fa").grid(row=5, column=0, sticky="w", pady=5)
date_entry = tk.Entry(form, width=30)
date_entry.grid(row=5, column=1)

# Register Button
register_btn = tk.Button(root, text="Register Ticket", command=register_ticket, bg="#4dd0e1", fg="white", font=("Arial", 12))
register_btn.pack(pady=20)

root.mainloop()