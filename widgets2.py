from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
root.title("CLOCK")

def msg():
    messagebox.showwarning("Alert","Stop it is a virus!")

button = Button(root, text="Click to open", command = msg)

button.place(x=55,y=70)

root.mainloop()