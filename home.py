import tkinter as tk
from datetime import datetime

class MainWindow:

    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.start_time = None

    def CreateWindow(self):
        window = tk.Tk()
        window.title(self.name)
        window.geometry(f"{self.height}x{self.width}")

        self.CreateMenuBar(window)

        button = tk.Button(window,text="Make a second window", command=self.donothing)
        button.pack()

        window.mainloop()

    def CreateMenuBar(self, window):
        menu_bar = tk.Menu(window)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.donothing)
        file_menu.add_command(label="Open", command=self.donothing)
        file_menu.add_command(label="Save", command=self.donothing)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Timelines")
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="View", menu=view_menu)
        window.config(menu=menu_bar)

    def donothing(self):
        if self.start_time == None:
            self.start_time = datetime.now()
        else:
            self.end_time = datetime.now()
            print((self.end_time - self.start_time))
            self.start_time = None