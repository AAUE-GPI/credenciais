import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


conn =sqlite3.connect('database_v1.db')
c = conn.cursor()

def create_table():
	c.execute('create table if not exists credenciais_DB(CodigoAlfaNum text, Nome text, BI_CC_Matricula text, tipo_user text)')

def clearDB():
	c.execute('drop table credenciais_DB')	

def data_entry():
	BI = input("Numero de identificacao: ")
	Nome = input("Primeiro e último nome: ")
	tipo_user = ''
	t_user = True

	################# Def tipo_user #################
	while t_user==True:
		
		z = input('Escolhe uma das seguintes opcoes:\n'
				  '[1] Nucleos\n'
				  '[2] Veiculos\n'
				  '[3] Artista\n'
				  '[4] Som\n'
				  '[5] etc\n')
		if z == '1':
			tipo_user = 'Nucleos'
			t_user = False
		elif z == '2':
			tipo_user = 'Veiculo'
			t_user = False
		elif z == '3':
			tipo_user = 'Artista'
			t_user = False
		elif z == '4':
			tipo_user = 'Som'
			t_user = False
		elif z == '5':
			tipo_user = 'etc'
			t_user = False
		else:
			print('Escolhe uma das opcoes possiveis')



################# Gerar Codigo AlfaNum #################

	number = '0123456789'
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	id = ''
	di = ''
	for i in range(0, len(tipo_user), 2):
		id += random.choice(number)
		id += random.choice(alpha)
	for i in range(0, len(tipo_user), 2):
		di += random.choice(number)
		di += random.choice(alpha)

	unix = str(time.time())
	if '.' in str(unix):
		unix_dec = str(unix).split('.')[-1]
		print(unix_dec)

	AlfaNum = str(id + unix_dec + di)
#	AlfaNum = '123456'


	##################################


	c.execute("insert into credenciais_DB(CodigoAlfaNum, Nome, BI_CC_Matricula, tipo_user) values (?, ?, ?,?)", (AlfaNum, Nome, BI, tipo_user))
	conn.commit()
	add_loop()


def add_loop():
	q = input('Queres adicionar mais?(S/n) ')
	if q=='s' or q=='S' or q=='':
		data_entry()
	elif q=='n' or q=='N':
		pass
	else:
		print('So tens duas opçoes burro!! Escolhe uma dessas')
		add_loop()
######################################################################

def remove():
	y = str(input('Remove:  '))

	c.execute('delete from credenciais_DB where CodigoAlfaNum = ?', y)
	conn.commit()






##########################################################################
def edit():
	e = input('Editar:\n'
			  '[1] Primeiro Nome\n'
			  '[2] BI/CC/Matricula\n'
			  '[3] Tipo de User\n')
	if e == '1':
		edit_Pnome()
#	elif e == '2':
#		edit_Unome()
#	elif e == '3':
#		edit_BI_CC_Matricula()
#	elif e == '4':
#		edit_tipo_user()
	else:
		edit()

def edit_Nome():

	new = (input('Nome (Novo): '),)
	old = (input('Nome (antigo): '),)
	codigo = (input('Codigo AlfaNum: '),)


#	c.execute('select * from credenciais_DB')
	c.execute('update credenciais_DB set Nome = ? WHERE Nome= ? and CodigoAlfaNum = ? ', (str(new), str(old), str(codigo)))
	conn.commit()


	c.execute('select * from credenciais_DB')
	[print(row) for row in c.fetchall()]


'''
	c.execute("update credenciais_DB set Pnome = 'paipau' WHERE Pnome='cona' and CodigoAlfaNum='0B0P40730217I3T'")
	conn.commit()

	c.execute('select * from credenciais_DB')
	[print(row) for row in c.fetchall()]

'''





'''
def edit_Unome():
	t = (input('Primeiro Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE Unome=?', t)
	print(c.fetchone())

def edit_BI_CC_Matricula():
	t = (input('Primeiro Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE BI_CC_Matricula=?', t)
	print(c.fetchone())

def edit_tipo_user():
	t = (input('Primeiro Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE tipo_user=?', t)
	print(c.fetchone())
'''

# c.execute('update pau set value = 99 where value = 8')
# conn.commit()


####################### Search #######################################

def search():
	s = input('Procurar por:\n'
			  '[1] Nome\n'
			  '[2] BI/CC/Matricula\n'
			  '[3] Tipo de User\n'
			  '[4] Codigo AlfaNum\n')
	if s == '1':
		search_Nome()
	elif s == '2':
		search_BI_CC_Matricula()
	elif s == '3':
		search_tipo_user()
	elif s == '4':
		search_CodigoAlfaNum()
	else:
		search()

def search_Nome():
	t = (input('Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE Nome=?', t)
	print(c.fetchone())

def search_BI_CC_Matricula():
	t = (input('Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE BI_CC_Matricula=?', t)
	print(c.fetchone())

def search_tipo_user():
	t = (input('Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE tipo_user=?', t)
	print(c.fetchone())

def search_CodigoAlfaNum():
	t = (input('Nome: '),)
	c.execute('SELECT * FROM credenciais_DB WHERE CodigoAlfaNum=?', t)
	print(c.fetchone())



########################################################################



def read_all_db():
	c.execute('Select * from credenciais_DB')
	print('Tamanho da Bases de Dados: '+str(len(c.fetchall()))+' Entradas')
	c.execute('Select * from credenciais_DB')
	for row in c.fetchall():
		print(row)
	print(50*'#')



############################## Master_loop ##############################


def master_loop():
	create_table()

	w = input('Escolhe uma das seguintes opcoes: \n'
			  '[1] Adicionar dados\n'
			  '[2] Remover dados\n'
			  '[3] Editar dados\n'
			  '[4] Procurar\n'
			  '[5] Ver toda da BD\n'
			  '[6] Limpar a BD\n')

	if w == '1':
		data_entry()
	elif w == '2':
		remove()
	elif w == '3':
		edit()
	elif w == '4':
		search()
	elif w == '5':
		read_all_db()
	elif w =='6':
		clearDB()
	else:
		print('Escolhe uma das opcoes possiveis')
		print(20*'\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/   \n')
		master_loop()


master_loop()
c.close()
conn.close()