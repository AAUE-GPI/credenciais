#Python OOP training/tkinter Sebastiao Pereira ex13745
#test1

class main_class:


	def __init__(self, attribute1, attribute2):
		super(main_class, self).__init__()
		self.attribute1 = attribute1
		self.attribute2 = attribute2
	
	def some_function(self):
		return('{} {}'.format(self.attribute1, self.attribute1))

var1 = main_class("STUFF FROM attribute1", "STUFF FROM attribute2")

var2 = main_class("STUFF FROM attribute1", "STUFF FROM attribute2")


#print(var1.attribute1)
#print(var2.attribute1)

#print(var1.some_function())
#print(main_class.some_function(var1))