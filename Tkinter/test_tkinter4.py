#Sebastiao Pereira ex13745
from tkinter import *

root = Tk()
root.title("Teste janela v0.04")



def printHello(event):
	print("Hello World!")

buttonOne = Button(root, text="Print my name")
buttonOne.bind("<Button-1>", printHello)
buttonOne.pack()


root.mainloop()
"""
"root" = name of the window
"root".title = title of the window
bg = background color
fg = font color

pack = the pack packs stuff on a windows it has some arguments that you can input
pack(side=SIDE) = it ensures that an object stay on a certain side
pack(fill=X/Y) = it fill the remaing space of a window with that object

entry = input

grid = the grid packs stuff like pack but it works with a grid instead of sides
grid(row,column)
grid(sticky) = it is like the fill in pack but it uses N(north), S(south), E(east), W(west)

bind(event, function)
"""