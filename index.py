import tkinter as tk
from tkinter import messagebox
import second_window

def donothing():
    ...

def make_new_window():
    new_window = second_window.secondWindow()
    new_window.make_window()


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

button = tk.Button(window,text="Make a second window", command=make_new_window)
button.pack()

window.mainloop()