#Sebastiao Pereira ex13745
from tkinter import *

root = Tk()
root.title("Teste janela v0.05")


def printRight(event):
	print("Hello Right!")


def printMiddle(event):
	print("Hello Middle!")


def printLeft(event):
	print("Hello LEFT!")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", printLeft)
frame.bind("<Button-2>",  printMiddle)
frame.bind("<Button-3>", printRight)
frame.pack()


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