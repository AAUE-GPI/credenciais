import sqlite3
import random

conn =sqlite3.connect('database.db')
c = conn.cursor()

def clearDB():
	c.execute('drop table credenciais_DB')

def create_table():
	c.execute('create table if not exists credenciais_DB(CodigoAlfaNum text, Nome text, BI_CC_Matricula text, tipo_user text)')

def adicionar(Nome,BI,tipo):
	c.execute("select CodigoAlfaNum from credenciais_DB where Nome='"+Nome+"';")
	data=c.fetchall()
	if data==[]:
		AlfaNum=CodigoAlfaNum()
		c.execute("insert into credenciais_DB(CodigoAlfaNum, Nome, BI_CC_Matricula, tipo_user) values (?, ?, ?,?)", (AlfaNum, Nome, BI, tipo))
	else:
		AlfaNum=data[0][0]
		c.execute("update credenciais_DB set Nome=?,BI_CC_Matricula=?,tipo_user=? where CodigoAlfaNum=?",(Nome,BI,tipo,AlfaNum))
	conn.commit()
	return AlfaNum

def CodigoAlfaNum():
    caracter= '0A0KU1B1L2V2CM3W3D4NX4EO5Y5F6PZ6G7Q7H8R8IS9JT9'
    AlfaNum='QF17'
    for i in range(0,8):
        AlfaNum += random.choice(caracter)
    return AlfaNum

def getbyname(name):
	c.execute('select * from credenciais_DB where Nome like "%'+name+'%";')
	return c.fetchall()

def getbyid(bi):
	c.execute('select * from credenciais_DB where BI_CC_Matricula like "%'+bi+'%";')
	return c.fetchall()

def getbyboth(name,bi):
	c.execute('select * from credenciais_DB where BI_CC_Matricula like "%'+bi+'%" and Nome like "%'+name+'%";')
	return c.fetchall()

def getbyall(cod,name,bi,tipo):
	c.execute('select * from credenciais_DB where BI_CC_Matricula="'+bi+'" and Nome="'+name+'" and CodigoAlfaNum="'+cod+'" and tipo_user="'+tipo+'";')
	return c.fetchall()

create_table()
