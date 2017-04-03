#Sebastiao Pereira ex13745
from tkinter import *
import tkinter.messagebox, random

root = Tk()

tkinter.messagebox.showinfo('Window Title', "stuff...")
r = random.randrange(1,15)
for i in range(r):
	answer = tkinter.messagebox.askquestion("Question1(y/n)", "Question")
	if answer == "yes":
		print("You can do stuff")
	elif answer == "no":
		print("This could be something aswell")
	else:
		print("Error message!")

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
padx/y = padding for the button
"""
