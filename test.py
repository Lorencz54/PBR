import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")

class EntryWithLimit(ttk.Entry):
    def __init__(self, master, max_length, **kw):
        super().__init__(master, **kw)

        self.max_length = max_length

        float_checker = root.register(self.is_valid_input)
        self.configure(validate="key", validatecommand=(float_checker, "%P"))

    def is_valid_input(self, text):
        if self.max_length:
            if len(text) > self.max_length:
                return False

        try:
            # Try converting the entered text to a float
            float(text)
            return True
        except ValueError:
            # If conversion fails, it's not a valid float
            return False

entry_float = EntryWithLimit(root, max_length=5)
entry_float.pack(expand=True)

root.mainloop()
