from tkinter import *
from tkinter import font,ttk
#from db import *
from PIL import Image, ImageTk

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.font1=font.Font(family='DejaVu Sans',size=22)      #Letra utilizada

        self.buttonstyle = ttk.Style()                                                                              #Estilo dos butões
        self.buttonstyle.configure('TButton',background='#575757',foreground='white',font=self.font1,relief=FLAT)   #Estilo dos butões
        self.buttonstyle.map('TButton',background=[('active', '#646464')])                                          #Estilo dos butões

        self.entrystyle=ttk.Style().configure("TEntry", bg='#2B2B2B', foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT, width = 50)   #Estilo das Entries(não surtiu efeito quando exprimentei)

        self.listusr=StringVar()        #variavel que vai guardar o tipo de utilizador

        #design#
        self.aaue=PhotoImage(file='logo.png')
        Label(self.master, image=self.aaue,bd=0).place(x=200,y=20)
        self.nome = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT).place(x=50,y=200,height=40,width=400)
        self.bi = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT).place(x=50,y=290,height=40,width=400)
        self.tipo = OptionMenu(self.master,self.listusr,'Nucleos','Veiculos','Artista','Som','etc')
        self.tipo.config(bg='#2B2B2B',bd=0,relief=FLAT,fg='white',font=self.font1)
        self.tipo['menu'].config(bg='#2B2B2B',bd=0,relief=FLAT,fg='white',font=self.font1)
        self.tipo.place(x=50,y=380,height=40,width=400)
        self.img = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT).place(x=50,y=470,height=40,width=400)
        self.addtogroup = ttk.Button(self.master,style='TButton',text="Adicionar a Grupo").place(x=75,y=560, width=350)     #adicionar o command para a função adicionar()
        self.grupoatual = Label(self.master,text="Grupo Atual: 0",bg='#2B2B2B',fg='#ffffff').place(x=200,y=610,height=30)
        self.gerar = ttk.Button(self.master,text="Gerar",style='TButton').place(x=75,y=710,width=350)   #adicionar o command para a função gerar()
        sep=ttk.Separator(self.master,orient=VERTICAL).place(x=500,y=100,height=582)
        self.search=Entry(self.master,font=self.font1).place(x=550,y=30,height=40,width=400)
        self.imgpreview=Label(self.master,bg='#000000').place(x=540,y=90,height=595,width=420)
        self.preview = ttk.Button(self.master,text="Preview",style='TButton').place(x=575,y=710,height=40,width=350)    #adicionar o command para a função preview()

    def check_entries(self):
        nome=self.nome.get()
        bi=self.bi.get()
        tipo=self.tipo.get()
        img=self.img.get()


def main():
    root = Tk()
    root.configure(background='#2B2B2B')
    root.title('Gestor de Credenciais')
    root.geometry('1000x782')
    root.resizable(width=False,height=False)
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()
