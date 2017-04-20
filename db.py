import sqlite3
import random

conn =sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
	c.execute('create table if not exists credenciais_DB(CodigoAlfaNum text, Nome text, BI_CC_Matricula text, tipo_user text)')

def adicionar(Nome,BI,tipo):
	AlfaNum=CodigoAlfaNum()
	c.execute("insert into credenciais_DB(CodigoAlfaNum, Nome, BI_CC_Matricula, tipo_user) values (?, ?, ?,?)", (AlfaNum, Nome, BI, tipo))
	conn.commit()

def CodigoAlfaNum():
    caracter= '0A0KU1B1L2V2CM3W3D4NX4EO5Y5F6PZ6G7Q7H8R8IS9JT9'
    AlfaNum='QF17'
    for i in range(0,8):
        AlfaNum += random.choice(caracter)
    return AlfaNum

def getbyname(name):
	get="select ? from credenciais_DB where Nome like ?"
	getnome=get+str(name+'%')
	c.execute(get, ('nome',(name+'%',)))
	nome=c.fetchone()
	bi=c.execute("select BI_CC_Matricula from credenciais_DB where Nome like ?",+name+"%")
	tipo=c.execute("select tipo_user from credenciais_DB where Nome="+name+"%")
	codig=c.execute("select CodigoAlfaNum from credenciais_DB where Nome="+name+"%")

name='Lui'
get="select ? from credenciais_DB where Nome like ?"
getnome=get+str(name+'%')
c.execute(getnome)
nome=c.fetchone()
print(nome)
