#Sebastiao Pereira ex13745
from tkinter import *

root = Tk()
root.title("Teste janela v0.02")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

buttonOne = Button(topFrame, text="Button 1", fg="red")
buttonOne.pack()
buttonTwo = Button(topFrame, text="Button 2", fg="blue")
buttonTwo.pack()
buttonThree = Button(topFrame, text="Button 3", fg="yellow")
buttonThree.pack()
buttonFour = Button(bottomFrame, text="Button 4", fg="green")




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