from tkinter import *
from PIL import Image as img
from tkinter import filedialog
import os, random

class main(object):
	"""docstring for main"""
	def __init__(self, arg):
		super(main, self).__init__()
		self.arg = arg
		


def do_nothing():
	print("FU this message is shit!")

def imagen_open_dialog():
	root.pic_file = filedialog.askopenfilename(title="Seleciona fotografia", filetypes=(("Jpg","*.jpg"),("Jpeg","*.jpeg"),("Png","*.png"),("all files","*.*")))

def imagen_save_dialog():
	root.sav_pic = filedialog.asksaveasfilename(title="Seleciona onde queres guardar o ficheiro", filetypes=(("Jpg","*.jpg"),("Jpeg","*.jpeg"),("Png","*.png"),("all files","*.*")))

def start():
	root = Tk()
	root.title("CredMaker AAUE-GPI")
	#çena do grupo
	name_var = StringVar()
	textbox1 = Entry(root, textvariable=name_var, text="Name:")
	id_var = StringVar()
	textbox2 = Entry(root, textvariable=id_var, text="B.I/C.C/N.M:")
	type_var = StringVar()
	textbox3 = Entry(root, textvariable=type_var, text="Tipo de Utilizador:")
	button_preview = Button(root, text="Preview the Photo")
	button_preview.bind("<Button-1>", preview_img)

	button_preview.pack()
	textbox1.pack()
	textbox2.pack()
	textbox3.pack()
	root.mainloop()

def check_acesso():
	main = Tk()
	main.title("Acesso")
	a1 = StringVar()
	a2 = StringVar()
	a3 = StringVar()
	a4 = StringVar()
	a5 = StringVar()
	a6 = StringVar()
	a7 = StringVar()
	button_a1 = Checkbutton(main, text="Area1", variable = a1, onvalue = "1", offvalue = "X")
	button_a2 = Checkbutton(main, text="Area2", variable = a2, onvalue = "2", offvalue = "X")
	button_a3 = Checkbutton(main, text="Area3", variable = a3, onvalue = "3", offvalue = "X")
	button_a4 = Checkbutton(main, text="Area4", variable = a4, onvalue = "4", offvalue = "X")
	button_a5 = Checkbutton(main, text="Area5", variable = a5, onvalue = "5", offvalue = "X")
	button_a6 = Checkbutton(main, text="Area6", variable = a6, onvalue = "6", offvalue = "X")
	button_a7 = Checkbutton(main, text="Area7", variable = a7, onvalue = "7", offvalue = "X")
	
	button_a1.pack()
	button_a2.pack()
	button_a3.pack()
	button_a4.pack()
	button_a5.pack()
	button_a6.pack()
	button_a7.pack()
	main.mainloop()
	acesso(a1,a2,a3,a4,a5,a6,a7)


def acesso(a1,a2,a3,a4,a5,a6,a7):
	draw.rectangle(((200,170),(235,205)), fill="red", outline = "white")
	draw.text((200+13, 170+6),a1,(0,0,0),font=font, fill="black")
	draw.rectangle(((235,170),(270,205)), fill="red", outline = "white")
	draw.text((235+13, 170+6),a2,(0,0,0),font=font, fill="black")
	draw.rectangle(((270,170),(305,205)), fill="red", outline = "white")
	draw.text((270+13, 170+6),a3,(0,0,0),font=font, fill="black")
	draw.rectangle(((305,170),(340,205)), fill="red", outline = "white")
	draw.text((305+13, 170+6),a4,(0,0,0),font=font, fill="black")
	draw.rectangle(((200+35/2,205),(235+35/2,240)), fill="red", outline = "white")
	draw.text((200+35/2+13, 205+6),a5,(0,0,0),font=font, fill="black")
	draw.rectangle(((235+35/2,205),(270+35/2,240)), fill="red", outline = "white")
	draw.text((235+35/2+13, 205+6),a6,(0,0,0),font=font, fill="black")
	draw.rectangle(((270+35/2,205),(305+35/2,240)), fill="red", outline = "white")
	draw.text((270+35/2+13, 205+6),a7,(0,0,0),font=font, fill="black")


def preview_img(foto):
	pic_file = filedialog.askopenfilename(title="Seleciona fotografia", filetypes=(("Jpg","*.jpg"),("Jpeg","*.jpeg"),("Png","*.png"),("all files","*.*")))
	pic = img.open(pic_file)
	pic.show()

def retrieve_input(textbox1,textbox2,textbox3):
	for i in [textbox1,textbox2,textbox3]:#fazer isto diferente
		input = myText_Box.get("1.0",END)

#start()

check_acesso()
"""
#image viewer widget
img = PhotoImage(file="logo2.png")
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")#trocar pois estamos a utilizar grid ou trocar td por pack :)


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=menu.new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=menu.quit)


#Check button
Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

def image(photo):
	img = Image.open(photo)
	draw = ImageDraw.Draw(img)
	width, height = img.size
	font = ImageFont.truetype("ariblk.ttf", 15)
	w, h = font.getsize("1")

"""