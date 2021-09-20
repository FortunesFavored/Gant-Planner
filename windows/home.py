import tkinter as tk
from tkinter import messagebox
import PopOut

def donothing():
    print('test')

def make_new_window():
    ...
    # new_window = PopOut.secondWindow()
    # new_window.make_window()

class MainWindow:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def CreateWindow(self):
        window = tk.Tk()
        window.geometry(f"{self.height}x{self.width}")
        self.CreateMenuBar(window)
        # menu_bar = tk.Menu(window)
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # file_menu.add_command(label="New", command=donothing)
        # file_menu.add_command(label="Open", command=donothing)
        # file_menu.add_command(label="Save", command=donothing)
        # file_menu.add_separator()
        # file_menu.add_command(label="Exit", command=window.quit)
        # menu_bar.add_cascade(label="File", menu=file_menu)
        # window.config(menu=menu_bar)

        button = tk.Button(window,text="Make a second window", command=make_new_window)
        button.pack()

        window.mainloop()

    def CreateMenuBar(self, window):
        menu_bar = tk.Menu(window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=donothing)
        file_menu.add_command(label="Open", command=donothing)
        file_menu.add_command(label="Save", command=donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        window.config(menu=menu_bar)