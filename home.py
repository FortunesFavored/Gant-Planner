import tkinter as tk
from datetime import datetime, time
import random


class MainWindow:

    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.running = True
        self.CreateWindow()

    def CreateWindow(self):
        self.window = tk.Tk()
        self.window.title(self.name)
        self.window.geometry(f"{self.height}x{self.width}")

        self.CreateMenuBar()

        self.lbl_result = tk.Label()
        self.label_a = tk.Label(master=self.window)
        self.button1 = tk.Button(master=self.window,text="Start the clock", command=self.StartRunning)

        self.proj_lst_frame = tk.Frame(self.window)


        self.button = tk.Button(master=self.proj_lst_frame,text="Make a second self.window", command=self.donothing)

        self.button1.pack()
        self.lbl_result.pack()

        self.proj_lst_frame.pack()
        self.button.pack()
        self.label_a.pack()

        self.window.mainloop()

    def CreateMenuBar(self):
        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.donothing)
        self.file_menu.add_command(label="Open", command=self.donothing)
        self.file_menu.add_command(label="Save", command=self.donothing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.quit)
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Timelines")
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.window.config(menu=self.menu_bar)

    def StartRunning(self):
        self.running = True
        self.start_time = datetime.now()
        self.StartTimer()

    def StartTimer(self):
        if self.running == True:
            self.current_time = datetime.now()
            # print(type(self.current_time))
            # print(type(self.start_time))
            # print(self.current_time)
            # print(self.start_time)
            self.button1.config(text="Stop the clock", command=self.EndTimer)
            self.lbl_result.config(text= self.current_time - self.start_time)
            self.lbl_result.after(10, self.StartTimer)

        # self.lbl_result['text'] = datetime.now()

    def EndTimer(self):
        self.running = False
        self.end_time = datetime.now()
        self.lbl_result['text'] = self.end_time - self.start_time
        self.button1.config(text="Start the clock", command=self.StartRunning)

    def donothing(self):
        if self.start_time == 0:
            self.start_time = datetime.now()
        else:
            self.end_time = datetime.now()
            self.start_time = 0