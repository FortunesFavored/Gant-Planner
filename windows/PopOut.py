import tkinter as tk
from tkinter import messagebox

class secondWindow:
    def __init__():
        window = tk.Tk()

        menu_bar = tk.Menu(window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.donothing)
        file_menu.add_command(label="Open", command=self.donothing)
        file_menu.add_command(label="Save", command=self.donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        window.config(menu=menu_bar)

        window.mainloop()

    def donothing():
        ...
