import tkinter as tk
from tkinter import messagebox

def show_warning_window():
    result = messagebox.askquestion("Warning", "Are you sure you want to proceed?")
    if result == 'yes':
        # Perform the action when 'Yes' is clicked
        print("Proceeding...")
    else:
        # Perform the action when 'No' is clicked or the window is closed
        print("Cancelled")

# Create the main Tkinter window
root = tk.Tk()
root.title("Tkinter Warning Window Example")

# Create a button that will trigger the warning window
warning_button = tk.Button(root, text="Show Warning", command=show_warning_window)
warning_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
