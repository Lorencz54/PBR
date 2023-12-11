import tkinter as tk

class UnderlineLabel(tk.Text):
    def __init__(self, master=None, **kwargs):
        tk.Text.__init__(self, master, wrap="none", **kwargs)
        self.tag_configure("underline", underline=True)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def set_text(self, text):
        self.delete("1.0", "end")
        self.insert("1.0", text)

    def underline(self, start, end):
        self.tag_add("underline", f"1.{start}", f"1.{end}")

    def on_enter(self, event):
        self.configure(cursor="hand2")

    def on_leave(self, event):
        self.configure(cursor="")

# Example usage
root = tk.Tk()

underline_label = UnderlineLabel(root, height=1, width=20, font=("Helvetica", 12))
underline_label.set_text("Underline Me")
underline_label.underline(0, 9)  # Underline characters 0 to 9
underline_label.pack(pady=20)

root.mainloop()
