from tkinter import *
from tkinter import font,ttk,messagebox
import db

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.grupos={1:0,2:0,3:0,4:0,5:0,6:0,7:0}      #dicionario para controlar os grupos

        self.font1=font.Font(family='DejaVu Sans',size=22)      #Letra utilizada

        self.buttonstyle = ttk.Style()                                                                              #Estilo dos butões
        self.buttonstyle.configure('TButton',background='#575757',foreground='white',font=self.font1,relief=FLAT)   #Estilo dos butões
        self.buttonstyle.map('TButton',background=[('active', '#646464')])                                          #Estilo dos butões
        self.grouppbuttonstyle = ttk.Style()                                                                        #Estilo dos butões de grupos pressionados
        self.grouppbuttonstyle.configure('pressed.TButton',background='#000080',foreground='white',font=self.font1,relief=SUNKEN)   #Estilo dos butões de grupos pressionados
        self.grouppbuttonstyle.map('pressed.TButton',background=[('active', '#0000ff')])                                           #Estilo dos butões de grupos pressionados
        self.groupubuttonstyle = ttk.Style()                                                                        #Estilo dos butões de grupos nao pressionados
        self.groupubuttonstyle.configure('unpressed.TButton',background='#575757',foreground='white',font=self.font1,relief=FLAT)   #Estilo dos butões de grupos nao pressionados
        self.groupubuttonstyle.map('unpressed.TButton',background=[('active', '#646464')])                                           #Estilo dos butões de grupos nao pressionados


        self.entrystyle=ttk.Style().configure("TEntry", bg='#2B2B2B', foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT, width = 50)   #Estilo das Entries(não surtiu efeito quando exprimentei)

        self.listusr=StringVar()        #variavel que vai guardar o tipo de utilizador

        #design#
        self.aaue=PhotoImage(file='logo.png')
        Label(self.master, image=self.aaue,bd=0).place(x=200,y=20)

        Label(self.master, text="Nome",font=('Helvetica',14),bg='#2B2B2B',fg='#ffffff').place(x=50,y=180)
        self.nome = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT)
        self.nome.place(x=50,y=200,height=40,width=400)

        Label(self.master, text="BI/CC/Matrícula",font=('Helvetica',14),bg='#2B2B2B',fg='#ffffff').place(x=50,y=270)
        self.bi = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT)
        self.bi.place(x=50,y=290,height=40,width=400)

        Label(self.master, text="Tipo de utilizador",font=('Helvetica',14),bg='#2B2B2B',fg='#ffffff').place(x=50,y=360)
        self.tipo = OptionMenu(self.master,self.listusr,'Nucleos','Veiculos','Artista','Som','etc')
        self.tipo.config(bg='#2B2B2B',bd=0,relief=FLAT,fg='white',font=self.font1)
        self.tipo['menu'].config(bg='#2B2B2B',bd=0,relief=FLAT,fg='white',font=self.font1)
        self.tipo.place(x=50,y=380,height=40,width=400)

        Label(self.master, text="Imagem de Fundo",font=('Helvetica',14),bg='#2B2B2B',fg='#ffffff').place(x=50,y=450)
        self.img = Entry(self.master,bg='#2B2B2B',foreground="#ffffff",font=self.font1,borderwidth=0,relief=FLAT)
        self.img.place(x=50,y=470,height=40,width=400)
        self.adicionar = ttk.Button(self.master,text="Gerar",style='TButton',command=self.add).place(x=75,y=550,width=350)   #adicionar o command para a função gerar()

    def add(self):
        db.adicionar(self.nome.get(),self.bi.get(),self.listusr.get())

def main():
    root = Tk()
    root.configure(background='#2B2B2B')
    root.title('Gestor de Credenciais')
    root.geometry('500x650')
    root.resizable(width=False,height=False)
    app = Application(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()
