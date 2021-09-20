import tkinter as tk
from tkinter import messagebox

class secondWindow:
    def donothing():
        ...

    def make_window(self):

        window = tk.Tk()

        menu_bar = tk.Menu(window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=donothing)
        file_menu.add_command(label="Open", command=donothing)
        file_menu.add_command(label="Save", command=donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        window.config(menu=menu_bar)

        window.mainloop()