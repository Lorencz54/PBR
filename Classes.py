import customtkinter as ctk
from customtkinter import *
class EntryWithLimit(CTkEntry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)


        float_checker = master.register(self.is_valid_input)
        self.configure(validate="key", validatecommand=(float_checker, "%P"))


    def is_valid_input(self, text):
        # Allow backspace
        if text == "" or text == '\b':
            return True

        try:
            float(text)
            return True
        except ValueError:
            return False
