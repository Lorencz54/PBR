import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Tkinter Entry List Example")
def function():
    entry.grid(row=2, column=1)
label = tk.Label(window, text="text")
label.grid(row=1, column=1)
entry = tk.Entry(window)
entry.grid(row=0, column=1)
button = tk.Button(window, command=function)
button.grid(row=3, column=1)
# Start the Tkinter event loop
window.mainloop()
