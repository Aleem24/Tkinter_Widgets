from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Adding a Image")
root.geometry("400x400")


upload = Image.open("image.png")


image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=700, width=1200)
label.place(x=50,y=0)
label.pack()

label2 = Label(root, text="This is how we add image in GUI")
label2.place(x=40, y=360)
label2.pack()


root.mainloop()
