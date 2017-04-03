#Sebastiao Pereira ex13745
from tkinter import *

root = Tk()
root.title("Teste janela v0.03")


labelOne = Label(root, text="USERNAME:", bg="white", fg="black")
labelTwo = Label(root, text="PASSWORD:", bg="white", fg="black")
entryOne = Entry(root)
entryTwo = Entry(root)

labelOne.grid(row=0, sticky=E)
labelTwo.grid(row=1, sticky=E)

entryOne.grid(row=0, column=1)
entryTwo.grid(row=1, column=1)

checkBox = Checkbutton(root, text="Keep me logged in!")
checkBox.grid(columnspan=2)

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
"""