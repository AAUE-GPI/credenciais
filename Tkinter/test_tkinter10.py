from tkinter import *

root = Tk()

photo = PhotoImage(file="image.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()