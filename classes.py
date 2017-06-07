#Programing Knowledge 15 Classes and Self
#Programing Knowledge 16 Class Constructors (__init__) and Destructor (__del__)
#class is an extensible program template for creating objects providing initial values of states and implementations of behavior

class PersonVideo15:
	def setFullName(self, firstName, lastName): #self is a keyword for a function in a class.  Must have self keyword to define a function in a class as first argument.  It's a pointer or a self points to the class itself personName.
		self.firstName = firstName
		self.lastName = lastName
	def printFullName(self): #self is a keyword for a function in a class.  Must have self keyword to define a function in a class as first argument.  It's a pointer or a self points to the class itself personName.
		print(self.firstName+" "+self.lastName)
#define object name or instance name personName for the class Person.  personName is the keyword self in the class Person.
personName = PersonVideo15()
#member function setFullName() of the class personName=Person().  Assigns firstNameVideo15 and lastNameVideo15 variable to setFullName()
personName.setFullName("firstNameVideo15","lastNameVideo15")
#member function printFullName() of the class personName=Person().  Prints the setFullName.
personName.printFullName() #prints firstNameVideo15 lastNameVideo15

class PersonVideo16:
	def __init__(self, identify):
		self.identify = identify
		print("The initial introduction called at the start:  Our class is  created starting here by itself.  The object personName didn't call __init__")
	def __del__(self):
		print("The destruction delete called at the end:  Our class object is  destroyed.  The object personName didn't call __del__")
	def setFullName(self, firstName, lastName): #self is a keyword for a function in a class.  Must have self keyword to define a function in a class as first argument.  It's a pointer or a self points to the class itself personName.
		self.firstName = firstName
		self.lastName = lastName
	def printFullName(self): #self is a keyword for a function in a class.  Must have self keyword to define a function in a class as first argument.  It's a pointer or a self points to the class itself personName.
		print(self.firstName+ " " +self.lastName+ ",",self.identify) #for any member function or member variable of a class, we must use self.  Self indicates it's a member of a class itself personName.
#define object name or instance name personName for the class Person
#also, we initialize __init__'s identify variable with the number 5
personName = PersonVideo16(5)
#member function setFullName() of the class personName=Person().  Assigns FirstNameVideo16 and LastNameVideo16 variable to setFullName()
personName.setFullName("FirstNameVideo16","LastNameVideo16")
#member function printFullName() of the class personName=Person().  
personName.printFullName() #Prints FirstNameVideo16 LastNameVideo16, 5
#destructor __del__ is ran and the print statement is printed
#__del__(self) is run to end the class.  "The destruction delete called at the end:  Our class object is  destroyed.  The object personName didn't call __del__"