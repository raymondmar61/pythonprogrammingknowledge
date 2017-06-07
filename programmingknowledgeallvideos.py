#Programming Knowledge 2 Numbers and Math in Python, 3 Variables and Inputs, 4 Built-in Modules and Functions, 5 Save and Run Python files, 6 Strings, 7 Lists, 8 Python Slices or Slicing, 9 IF ELSE Statements, 10 elif and nested if Statements, 11 Comparison operators Logical Operators is and in, 12 While Loop and For Loops, 13 Defining Functions, 14 Default parameters and Multiple Arguments, 15 Classes and Self, 16 Class Constructors (__init__) and Destructor (__del__), 17 Subclasses Superclasses Inheritance

print(21/7) #print 3.0
print(21.0/7) #print 3.0
print(21//7) #print 3
print(2**15) #print 32768.  Exponent.

myVariable = 30
print(myVariable) #print 30
print(myVariable + 34) #print 64
#value = input("Enter the value: ")
#print(value)
#print(type(value)) #print <class 'str'>
#value = int(input("Enter the value: "))
#value = float(input("Enter the value: "))

print(pow(2,3)) #print 8
#print(dir(__builtins__)) #print built in functions used in Python.  For example, abs, print, pow, len, type, help.
#print(help(max)) #press q to exit the help function after search
import math
print(math.sqrt(9)) #print 3.0
squareRoot = math.sqrt
print(squareRoot(9)) #print 3.0

x = 22
y = 33
z = 44
print(max(x,y,z)) #print 44

a = 'I am a single quoted string don\'t'
b = "I am a double \"quoted\" string"
c = """I am a \\triple quoted string"""
b5 = 5
print(a) #print I am a single quoted string don't
print(b) #print I am a double "quoted" string
print(c) #print I am a \triple quoted string
print(len(a)) #print 33
print(a + b) #print I am a single quoted string don'tI am a double "quoted" string  concatenate.
print(a * 2) #print I am a single quoted string don'tI am a single quoted string don't
print(a + " " + str(b5)) #print I am a single quoted string don't 5

names = ["mark","john","july"]
print(names) #print ['mark', 'john', 'july']
print(names[0]) #print mark
print(names[2]) #print july
print(names[-1]) #print july
names.append("patrik")
print(names) #print ['mark', 'john', 'july', 'patrik']
age = [23,12,32,11]
names.extend(age)
print(names) #print ['mark', 'john', 'july', 'patrik', 23, 12, 32, 11]
names.remove("patrik")
print(names) #print ['mark', 'john', 'july', 23, 12, 32, 11]
print(len(names)) #print 7

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[4:8]) #print [4, 5, 6, 7]
print(mylist[5:9]) #print [5, 6, 7, 8]
print(mylist[5:10]) #print [5, 6, 7, 8, 9]
print(mylist[5:]) #print [5, 6, 7, 8, 9]
print(mylist[:10]) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist[:5]) #print [0, 1, 2, 3, 4]
print(mylist[-4:-2]) #print [6,7] Start at index -4 which is 6 and stop at  index -2 minus one which is 7
print(mylist[-6:]) #print [4, 5, 6, 7, 8, 9] Start at index -6 which is 4 and stop at the end of the list
print(mylist[0:10:2]) #print [0, 2, 4, 6, 8]
print(mylist[0:10:3]) #print [0, 3, 6, 9]
print(mylist[::3]) #print [0, 3, 6, 9]
print(mylist[::-2]) #print [9, 7, 5, 3, 1]
print(mylist[-2::-2]) #print [8, 6, 4, 2, 0]
print(mylist[::-3]) #print [9, 6, 3, 0]
namesletters = ["a","b","c","d"]
print(namesletters[2:3]) #print ['c']

#n = int(input("Number? "))
n = 5
if n < 0:
	print("The Absolute value of",n,"is",abs(n))
else:
	print("The Absolute value of",n,"is",n)
	sumoftwo = 50 + 60
	print(sumoftwo) #print 110

name = input("Name? ")
if name == "Mark":
	print("The Mname entered is " +name)
elif name == "John":
	print("The Jname entered is " +name)
elif name == "July":
	print("The Jname entered is " +name)
elif name == "Tom":
	print("The Tname entered is " +name)
else:
	print("The name entered is not valid")
name2 = "animal"
animalName = "cat"
if name2 == "animal":
	if animalName == "dog":
		print("Valid animal")
	elif animalName == "cat":
		print("Cute animal")
	else:
		print("It's an animal")
	print("name2 entered is "+name2)
else:
	print("The name2 entered is not valid")

if 9 > 10 and 9!= 10:
	print("and True")
else:
	print("and False") #print and False
if 9 > 10 or 9!= 10:
	print("or True") #print and True
else:
	print("or False")
string = "abcde"
if "abc" in string:
	print("yes") #print yes
else:
	print("no")
a = [1,2,3]
if 3 in a:
	print("True")  #print True
else:
	print("False")

aloop = 0
while aloop < 5:
	print(aloop) #print 0\n1\n2\n3\n4
	aloop+=1
b = 1 #initialize while loop
s = 0 #initialize while loop
print("Enter Numbers to add to the sum.")
print("Enter 0 to quit.")
while b != 0:
	print("Current Sum:", s)
	b = float(input("Number? "))
	b = float(b)
	s += b #s = s + b
print ("Total Sum =",s)
c = [3,4,5,2,3,7,6,5,4,3,2]
for eachc in c:
	print(eachc) #prints each number c in the list c in its own line
	pass

def hello(name):
	print("Hello "+name)
hello("Mark") #return Hello Mark
hello("John") #return Hello John
hello("July") #return Hello July
def add(x,y):
	return (x + y)
print(add(100,500)) #print 600
print(add(234,333)) #print 567

def studentScore(name="tom", score=0):
	print(name+ " scored",score,"marks")
studentScore("mark",70) #return mark scored 70 marks
studentScore() #return tom scored 0 marks
studentScore("mark") #return mark scored 0 marks
studentScore(score=99) #return tom scored 99 marks
def studentMultipleScores(name,*score):
	print(name)
	print(score)
studentMultipleScores("jim",55,77,90,67) #return jim \n(55,77,90,67)
def studentMultipleScoresAverage(name,*score):
	print(name)
	print(sum(score)/len(score))
studentMultipleScoresAverage("jim",55,77,90,67) #return jim \n72.25

class Person:
	def setFullName(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	def printFullName(self):
		print(self.firstName + " " + self.lastName)
personName = Person()
personName.setFullName("programming","knowledge")
personName.printFullName() #return programming knowledge

class Personvideo16:
	def __init__(self, identify):
		self.identify = identify
		print("Our class is created.  The initial function __init__ is called first initializing the value for Personvideo16 class.  It's called a Constructor." + str(self.identify))
	def __del__(self):
		print("Our class object is destroyed.  The deletion function __del__ is called when the class instance is out of scope.  Out of scope means the class instance is no longer used or class instance is completed.  It's called a Destructor. " + str(self.identify))
	def setFullName(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	def printFullName(self):
		print(self.firstName + " " + self.lastName)
personName = Personvideo16(16)
personName.setFullName("programming video 016","knowledge video 016")
personName.printFullName() #return see multiline comment below
"""return Our class is created.  The initial function __init__ is called first initializing the value for Personvideo16 class.  It's called a Constructor.16\n 
	programming video 016 knowledge video 016\n
	Our class object is destroyed.  The deletion function __del__ is called when the class instance is out of scope.  Out of scope means the class instance is no longer used or class instance is completed.  It's called a Destructor. 16
"""

class Parent12:
	value1 = "this is value 1 from Parent12 class"
	value2 = "this is value 2 from Parent12 class"
class Parent34:
	value3 = "this is value 3 from Parent34 class"
	value4 = "this is value 4 from Parent34 class"
class Child(Parent12, Parent34):
	pass
parentprintvalues = Parent12()
print(parentprintvalues.value1) #print this is value 1 from Parent12 class
print(parentprintvalues.value2) #print this is value 2 from Parent12 class
childprintparentvalues = Child()
print(childprintparentvalues.value1) #print this is value 1 from Parent12 class
print(childprintparentvalues.value2) #print this is value 2 from Parent12 class
print(childprintparentvalues.value4) #print this is value 4 from Parent34 class
