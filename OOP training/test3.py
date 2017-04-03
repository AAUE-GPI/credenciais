#Python OOP training/tkinter Sebastiao Pereira ex13745
#test3

class Employee:
	
	raise_amount = 1.04

	n_of_emps = 0

	def __init__(self, first, last, pay):
		super(Employee, self).__init__()
		self.first = first
		self.last = last
		self.pay=pay
		self.email = first + '.' + last + "@company"

		Employee.n_of_emps +=1 #good stuff for programmcounter

	def fullname(self):
		return('{} {}'.format(self.first, self.last))
	
	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)	
		

emp_1 = Employee('First Name', 'Last Name', 0)
emp_2 = Employee('test name', 'test last', 999)

print(Employee.__dict__)

#Employee.raise_amount = 1.05

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(emp_1.pay)

print(Employee.n_of_emps)