import tkinter as tk
from customtkinter import *
class EntryWithLimit(CTkEntry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        float_checker = master.register(self.is_valid_input)
        self.configure(validate="key", validatecommand=(float_checker, "%P"))

        # Set the initial value to "0.0"
        self.insert(0, "0.0")

        # Bind FocusIn and FocusOut events
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def is_valid_input(self, text):
        # Allow backspace
        if text == "" or text == '\b':
            return True

        try:
            float_value = float(text)
            return True
        except ValueError:
            return False

    def on_focus_in(self, event):
        if self.get() == 0.0:
            self.delete(0, tk.END)

    def on_focus_out(self, event):
        if self.get() == 0.0:
            self.insert(0, "0.0")

    def get(self):
        value = super().get()
        return float(value) if value else 0.0
