import tkinter as tk
from tkinter import ttk
import folium
import webbrowser
import threading
import time
import os

# Initial location (simulate train starting point)
train_lat = 28.6139
train_lon = 77.2090

def create_schedule_table(frame):
    columns = ("Train", "From", "To", "Time")
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=200)
    
    data = [
        ("aurangabad express", "guntur", "aurangabad", "7:35 AM"),
         ("okha superfast express", "tuticorin", "okha", "11:35 PM"),
        ("howrah superfast express", "jodhpur", "howrah junction", "11:55 PM")
    ]
    
    for item in data:
        tree.insert('', tk.END, values=item)
    
    tree.pack(pady=10)

def generate_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=6)
    folium.Marker(
        [lat, lon],
        popup="Train Location",
        icon=folium.Icon(color="blue", icon="train", prefix='fa')
    ).add_to(m)
    
    m.save("train_map.html")

def update_location():
    global train_lat, train_lon
    while True:
        train_lat += 0.1
        train_lon += 0.1
        generate_map(train_lat, train_lon)
        time.sleep(5)  # Update every 5 seconds

def open_map():
    webbrowser.open("train_map.html")

def start_tracking():
    generate_map(train_lat, train_lon)
    threading.Thread(target=update_location, daemon=True).start()
    open_map()

# Tkinter UI
root = tk.Tk()
root.title("Train Timing and Tracker")
root.geometry("1000x800")

label = tk.Label(root, text="Train Schedule", font=("Arial", 20))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

create_schedule_table(frame)

track_button = tk.Button(root, text="Start Tracking Train Location", command=start_tracking)
track_button.pack(pady=20)

root.mainloop()