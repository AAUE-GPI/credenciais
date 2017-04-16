from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
from tkinter import font,ttk,messagebox
from reportlab.lib.pagesizes import A4,A6
from reportlab.pdfgen import canvas
import random
from PIL import Image,ImageDraw,ImageFont

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

        self.group1 = ttk.Button(self.master,style='unpressed.TButton',text="1",command=self.switch(1))
        self.group1.place(x=150,y=560,width=50,height=50)
        self.group2 = ttk.Button(self.master,style='unpressed.TButton',text="2",command=self.switch(2))
        self.group2.place(x=200,y=560,width=50,height=50)
        self.group3 = ttk.Button(self.master,style='unpressed.TButton',text="3",command=self.switch(3))
        self.group3.place(x=250,y=560,width=50,height=50)
        self.group4 = ttk.Button(self.master,style='unpressed.TButton',text="4",command=self.switch(4))
        self.group4.place(x=300,y=560,width=50,height=50)
        self.group5 = ttk.Button(self.master,style='unpressed.TButton',text="5",command=self.switch(5))
        self.group5.place(x=175,y=610,width=50,height=50)
        self.group6 = ttk.Button(self.master,style='unpressed.TButton',text="6",command=self.switch(6))
        self.group6.place(x=225,y=610,width=50,height=50)
        self.group7 = ttk.Button(self.master,style='unpressed.TButton',text="7",command=self.switch(7))
        self.group7.place(x=275,y=610,width=50,height=50)

        self.gerar = ttk.Button(self.master,text="Gerar",style='TButton',command=self.gerar).place(x=75,y=710,width=350)   #adicionar o command para a função gerar()
        sep=ttk.Separator(self.master,orient=VERTICAL).place(x=500,y=100,height=582)
        self.search=Entry(self.master,font=self.font1)
        self.search.place(x=550,y=30,height=40,width=400)
        self.imgpreview=Label(self.master,bg='#000000').place(x=540,y=90,height=595,width=420)
        self.preview = ttk.Button(self.master,text="Preview",style='TButton').place(x=575,y=710,height=40,width=350)    #adicionar o command para a função preview()

    def switch(self,n):
        def wrapper(x=n):
            if x==1 and self.grupos[1]==0:
                self.group1.configure(style='pressed.TButton')
                self.grupos[1]=1
            elif x==1 and self.grupos[1]==1:
                self.group1.configure(style='unpressed.TButton')
                self.grupos[1]=0
            elif x==2 and self.grupos[2]==0:
                self.group2.configure(style='pressed.TButton')
                self.grupos[2]=1
            elif x==2 and self.grupos[2]==1:
                self.group2.configure(style='unpressed.TButton')
                self.grupos[2]=0
            elif x==3 and self.grupos[3]==0:
                self.group3.configure(style='pressed.TButton')
                self.grupos[3]=1
            elif x==3 and self.grupos[3]==1:
                self.group3.configure(style='unpressed.TButton')
                self.grupos[3]=0
            elif x==4 and self.grupos[4]==0:
                self.group4.configure(style='pressed.TButton')
                self.grupos[4]=1
            elif x==4 and self.grupos[4]==1:
                self.group4.configure(style='unpressed.TButton')
                self.grupos[4]=0
            elif x==5 and self.grupos[5]==0:
                self.group5.configure(style='pressed.TButton')
                self.grupos[5]=1
            elif x==5 and self.grupos[5]==1:
                self.group5.configure(style='unpressed.TButton')
                self.grupos[5]=0
            elif x==6 and self.grupos[6]==0:
                self.group6.configure(style='pressed.TButton')
                self.grupos[6]=1
            elif x==6 and self.grupos[6]==1:
                self.group6.configure(style='unpressed.TButton')
                self.grupos[6]=0
            elif x==7 and self.grupos[7]==0:
                self.group7.configure(style='pressed.TButton')
                self.grupos[7]=1
            elif x==7 and self.grupos[7]==1:
                self.group7.configure(style='unpressed.TButton')
                self.grupos[7]=0
        return wrapper

    def CodigoAlfaNum(self):
        caracter= '0A0KU1B1L2V2CM3W3D4NX4EO5Y5F6PZ6G7Q7H8R8IS9JT9'
        AlfaNum='QF17'
        for i in range(0,8):
            AlfaNum += random.choice(caracter)
        return AlfaNum

    def gerar(self):
        #self.gerarA6()
        self.gerarA4()
        messagebox.showinfo("Sucesso", "Credencial "+str(self.CodigoAlfaNum())+" criada com sucesso.")

    def gerarA6(self):
        from reportlab.lib.units import mm
        posx=60
        posy=100
        fich='credsA6/Credencial'+self.CodigoAlfaNum()+'.pdf'
        self.c=canvas.Canvas(fich,pagesize=A6)
        fundo='fundo.jpg' #escolher a imagem de fundo do pdf (sempre 300x424)
        self.c.drawImage(fundo,0,0)
        self.c.setFillColorRGB(1,1,1)
        self.c.rect(10*mm,85*mm,40*mm,5*mm, fill=1)             #caixa para o nome
        self.c.rect(10*mm,60*mm,40*mm,5*mm, fill=1)             #caixa para o bi/cc/Matricula
        self.c.rect(16.25*mm,20*mm,17.5*mm,17.5*mm, fill=1)     #caixa para o qrcode
        self.c.rect(10*mm,15*mm,30*mm,5*mm, fill=1)             #caixa para o codigo alfanumerico
        self.c.setFont("Helvetica", 10)
        for i in self.grupos:
            if self.grupos[i]==1:
                self.c.setFillColorRGB(1,1,1)
                self.c.rect(posx*mm,posy*mm,10*mm,10*mm,fill=1)
                self.c.setFillColorRGB(0,0,0)
                self.c.drawString((posx+4)*mm,(posy+4)*mm,str(i))
            if i!=4:
                posx+=10
            else:
                posx-=25
                posy-=10
        self.c.setStrokeColorRGB(0,0,0)
        self.c.setFillColorRGB(0,0,0)

        self.c.drawString(11.5*mm,86.25*mm,self.nome.get())
        self.c.drawString(11.5*mm,61.25*mm,self.bi.get())
        self.c.drawString(11*mm,16.1*mm,self.CodigoAlfaNum())

        self.c.drawString(10*mm,91*mm,'Nome:')
        self.c.drawString(10*mm,66*mm,'BI/CC/Matricula:')
        self.c.showPage()
        self.c.save()


    def gerarA4(self):
        from reportlab.lib.units import mm
        countmerged=int(open('cnt1').read())
        countfiles=int(open('cnt2').read())
        fich='credsA4/Credencialtemp.pdf'
        fundo='fundo.jpg' #escolher a imagem de fundo do pdf (sempre 300x424)
        self.c=canvas.Canvas(fich)
        if countmerged==4:
            countfiles+=1
            countmerged=0
        fname='credsA4/Credencial'+str(countfiles+1)+'.pdf'
        if countmerged==0:
            can=canvas.Canvas(fname)
            can.showPage()
            can.save()
            x=0
            y=148.5
        elif countmerged==1:
            x=105
            y=148.5
        elif countmerged==2:
            x=0
            y=0
        elif countmerged==3:
            x=105
            y=0
        posx=60
        posy=100
        printready=PdfFileReader(fname,'rb')
        page1=printready.getPage(0)
        self.c.drawImage(fundo,x*mm,y*mm)
        self.c.setFillColorRGB(1,1,1)
        self.c.rect((x+10)*mm,(y+85)*mm,40*mm,5*mm, fill=1)             #caixa para o nome
        self.c.rect((x+10)*mm,(y+60)*mm,40*mm,5*mm, fill=1)             #caixa para o bi/cc/Matricula
        self.c.rect((x+16.25)*mm,(y+20)*mm,17.5*mm,17.5*mm, fill=1)     #caixa para o qrcode
        self.c.rect((x+10)*mm,(y+15)*mm,30*mm,5*mm, fill=1)             #caixa para o codigo alfanumerico
        self.c.setFont("Helvetica", 10)
        for i in self.grupos:
            if self.grupos[i]==1:
                self.c.setFillColorRGB(1,1,1)
                self.c.rect((x+posx)*mm,(y+posy)*mm,10*mm,10*mm,fill=1)
                self.c.setFillColorRGB(0,0,0)
                self.c.drawString((x+posx+4)*mm,(y+posy+4)*mm,str(i))
            if i!=4:
                posx+=10
            else:
                posx-=25
                posy-=10
        self.c.setStrokeColorRGB(0,0,0)
        self.c.setFillColorRGB(0,0,0)

        self.c.drawString((x+11.5)*mm,(y+86.25)*mm,self.nome.get())
        self.c.drawString((x+11.5)*mm,(y+61.25)*mm,self.bi.get())
        self.c.drawString((x+11)*mm,(y+16.1)*mm,self.CodigoAlfaNum())

        self.c.drawString((x+10)*mm,(y+91)*mm,'Nome:')
        self.c.drawString((x+10)*mm,(y+66)*mm,'BI/CC/Matricula:')
        self.c.showPage()
        self.c.save()
        temp=PdfFileReader(open('credsA4/Credencialtemp.pdf','rb'))
        page2=temp.getPage(0)
        page1.mergePage(page2)
        output=PdfFileWriter()
        output.addPage(page1)
        output.write(open('credsA4/Credencial'+str(countfiles+1)+'.pdf','wb'))

        countmerged+=1
        open('cnt1','w').write(str(countmerged))
        open('cnt2','w').write(str(countfiles))

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
