import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')



conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('create table if not exists pau(unix real, datestamp text, keyword text, value real)')


def data_entry():
	c.execute("insert into pau VALUES(68541654685, '2017-Mar-03', 'python', 5)")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python3'
	value = random.randrange(0,10)
	c.execute("insert into pau(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",(unix, date, keyword, value))
	conn.commit()


def read_from_db():
	c.execute('Select * from pau where ')
	#data = c.fetchall()
	#print(data)
	for row in c.fetchall():
		print(row)


def graph_data():
	c.execute("select unix, value from pau")
	dates = []
	values = []
	for row in c.fetchall():
		#print(row[0])
		#print(datetime.datetime.fromtimestamp(row[0]))
		dates.append(datetime.datetime.fromtimestamp(row[0]))
		values.append(row[1])

	plt.plot_date(dates, values, '-')
	plt.show()


def del_and_update():
	c.execute('select * from pau')
	[print(row) for row in c.fetchall()]
	
	c.execute('select * from pau')
	print(len(c.fetchall()))
	print(75*'<')


	c.execute('update pau set value = 99 where value = 8')
	conn.commit()

	c.execute('select * from pau where value = 99')
	[print(row) for row in c.fetchall()]

	c.execute('select * from pau where value = 99')
	print(len(c.fetchall()))
	print(75*'#')


#	c.execute('delete from pau where value = 99')
#	conn.commit()
#	[print(row) for row in c.fetchall()]
#	print(75*'>')


	c.execute('select * from pau where value = 2')
	[print(row) for row in c.fetchall()]
	
	c.execute('select * from pau where value = 2')
	print(len(c.fetchall()))
	print(75*'+')

	c.execute('select * from pau where value = 2')
	for row in c.fetchall():
		print(row)









#################################

create_table()
#data_entry()

#for i in range(10):
#	dynamic_data_entry()
#	time.sleep(1)

#read_from_db()
graph_data()
del_and_update()
#################################


c.close()
conn.close()


