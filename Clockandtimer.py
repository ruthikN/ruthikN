import tkinter as tk
from tkinter import messagebox
import time

def countdown():
    # Get the time interval in seconds
    time_interval = int(entry.get())

    # Disable the entry and start button during the countdown
    entry.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)

    # Start the countdown
    while time_interval >= 0:
        mins, secs = divmod(time_interval, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        time.sleep(1)
        root.update()
        time_interval -= 1

    # Enable the entry and start button after the countdown is over
    entry.config(state=tk.NORMAL)
    start_button.config(state=tk.NORMAL)

    # Show a notification messagebox
    messagebox.showinfo("Countdown Timer", "Time's up!")

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")

# Create a label for the timer
label = tk.Label(root, text="00:00", font=("Arial", 24))
label.pack(pady=10)

# Create an entry for the time interval
entry = tk.Entry(root, font=("Arial", 16), justify='center')
entry.pack(pady=10)

# Create a start button to begin the countdown
start_button = tk.Button(root, text="Start", font=("Arial", 16), command=countdown)
start_button.pack(pady=10)

# Run the application
root.mainloop()
