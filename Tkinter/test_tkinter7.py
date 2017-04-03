#Sebastiao Pereira ex13745
from tkinter import *

def do_nothing():
	print("OK")

root = Tk()
root.title("Teste janela v0.07")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=do_nothing)
subMenu.add_command(label="New", command=do_nothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=menu.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=do_nothing)

toolbar = Frame(root, bg="blue")
Button1 = Button(toolbar, text="Insert Image", command=do_nothing)
Button1 = Button(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP,fill=X)

statusBar = Label(root,text="Status stuff...", bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


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