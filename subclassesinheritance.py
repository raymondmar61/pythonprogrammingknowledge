#ProgrammingKnowledge  17 Subclasses, Superclasses and Inheritance
#inheritance defines a class in terms of another class which makes it easier to maintain our application

class Parent1:
	value1 = "this is value 1"
	value2 = "this is value 2"
class Parent2:
	value3 = "this is value 3"
	value4 = "this is value 4"
class Child(Parent1, Parent2):
	pass

parent1 = Parent1()
print(parent1.value1) #prints this is value 1
print(parent1.value2) #prints this is value 2
print("----- child() class below inherit Parent1() class value1 and value2 variables")
child_ = Child()
print(child_.value1) #prints this is value 1
print(child_.value2) #prints this is value 2

parent2 = Parent2()
print(parent2.value3) #prints this is value 3
print(parent2.value4) #prints this is value 3
print("----- child() class below inherit Parent2() class value3 and value4 variables")
child_ = Child()
print(child_.value3) #prints this is value 3
print(child_.value4) #prints this is value 4