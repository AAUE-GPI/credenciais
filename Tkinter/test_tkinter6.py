#Sebastiao Pereira ex13745
from tkinter import *


class Buttons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)
		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)
	def printMessage(self):
		print("Hello!")

root = Tk()
root.title("Teste janela v0.06")
b = Buttons(root)
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