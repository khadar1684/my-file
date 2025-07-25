import tkinter as tk
from tkinter import messagebox

station_data = {
    'NDLS': {'name': 'New Delhi', 'state': 'Delhi', 'zone': 'Northern Railway'},
    'BCT': {'name': 'Mumbai Central', 'state': 'Maharashtra', 'zone': 'Western Railway'},
    'HWH': {'name': 'Howrah Junction', 'state': 'West Bengal', 'zone': 'Eastern Railway'},
    'MAS': {'name': 'Chennai Central', 'state': 'Tamil Nadu', 'zone': 'Southern Railway'},
    'SBC': {'name': 'Bangalore City', 'state': 'Karnataka', 'zone': 'South Western Railway'},
    'GNT': {'name': 'Guntur', 'state':'Andhra Pradesh', 'zone': 'South Central Railway'},
    'CSTM': {'name': 'Chhatrapati Shivaji Terminus', 'state': 'Maharashtra', 'zone': 'Central Railway'},
    'LKO': {'name': 'Lucknow', 'state': 'Uttar Pradesh', 'zone': 'Northern Railway'},
    'PUNE': {'name': 'Pune', 'state': 'Maharashtra', 'zone': 'Central Railway'},
    'SDAH': {'name': 'Secunderabad Junction', 'state': 'Telangana', 'zone': 'South Central Railway'},
    'JP': {'name': 'Jaipur', 'state': 'Rajasthan', 'zone': 'North Western Railway'},
    'GKP': {'name': 'Gorakhpur', 'state': 'Uttar Pradesh', 'zone': 'North Eastern Railway'},
    'KJM': {'name': 'Kacheguda', 'state': 'Telangana', 'zone': 'South Central Railway'},
    'BDTS': {'name': 'Bandra Terminus', 'state': 'Maharashtra', 'zone': 'Western Railway'},
    'NDM': {'name': 'Nanded', 'state': 'Maharashtra', 'zone': 'South Central Railway'},
    'RNC': {'name': 'Ranchi', 'state': 'Jharkhand', 'zone': 'South Eastern Railway'},
    'BBS': {'name': 'Bhubaneswar', 'state': 'Odisha', 'zone': 'East Coast Railway'},
    'MAO': {'name': 'Mangalore Central', 'state': 'Karnataka', 'zone': 'South Western Railway'},
    'AJJ': {'name': 'Arakkonam Junction', 'state': 'Tamil Nadu', 'zone': 'Southern Railway'}
    # Add more stations if needed...
}

def get_station_details():
    query = entry.get().strip().upper()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a station code or name.")
        return
    
    # Search by code
    if query in station_data:
        details = station_data[query]
        result_text = (
            f"Code: {query}\n"
            f"Name: {details['name']}\n"
            f"State: {details['state']}\n"
            f"Zone: {details['zone']}"
        )
        result_label.config(text=result_text)
        return
    
    # Search by station name
    for code, details in station_data.items():
        if details['name'].upper() == query:
            result_text = (
                f"Code: {code}\n"
                f"Name: {details['name']}\n"
                f"State: {details['state']}\n"
                f"Zone: {details['zone']}"
            )
            result_label.config(text=result_text)
            return
    
    # Not found case
    messagebox.showerror("Not Found", f"No details found for '{query}'")
    result_label.config(text="")

root = tk.Tk()
root.title("Railway Station Details")
root.geometry("600x600")
root.resizable(True, True)
root.config(bg="#f0f8ff")

tk.Label(root, text="Enter Station Code or Name:", font=("Arial", 14), bg="#f0f8ff", fg="#333333").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), bg="#e6f2ff", fg="#000000", bd=2, relief="groove")
entry.pack(pady=5)
entry.focus()

tk.Button(root, text="Search", command=get_station_details, font=("Arial", 12),
          bg="#4a90e2", fg="white", activebackground="#357ABD",
          activeforeground="white", bd=0, padx=10, pady=5).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left", bg="#f0f8ff", fg="#000000")
result_label.pack(pady=10)

root.mainloop()
