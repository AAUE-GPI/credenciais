#Sebastiao Pereira ex13745
from tkinter import *

root = Tk()
root.title("Teste janela v0.01")


labelOne = Label(root, text="Text1", bg="white", fg="black")
labelOne.pack()
labelTwo = Label(root, text="Text2", bg="white", fg="black")
labelTwo.pack(fill=X)
labelThree = Label(root, text="Text3", bg="white", fg="black")
labelThree.pack(side=LEFT,fill=Y)



root.mainloop()

"""
"root" = nome da janela
"root".title = titulo da janela
bg = background color
fg = font color

pack = the pack packs stuff on a windows it has some arguments that you can input
pack(side=SIDE) = it ensures that an object stay on a certain side
pack(fill=X/Y) = it fill the remaing space of a window with that object
"""