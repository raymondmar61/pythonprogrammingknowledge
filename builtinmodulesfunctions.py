#ProgrammingKnowledge 4 Built-in Modules and Functions
#ProgrammingKnowledge 5 Save and Run Python files .py

def expontentthree(x):
	print(x**3)
expontentthree(2) #return 8

print(pow(3,5)) #print 243, expontent pow(number, exponent)

#dir(__builtins__) in Python shell, shows all built-in functions; e.g. pow, abs, print, len
#help(build-in function) Python provides description; e.g. help(max)

#import module name is used to activate a built-in module; e.g. import math
import math

#type module name, then period.  See built-in options associated with module.  Some reason I see few built-in options in Sublime Text.  I believe I need to download a package. 
print(math.sqrt(16)) #print 4.0
squareRoot = math.sqrt
print(squareRoot(16)) #print 4.0
print(int(squareRoot(16))) #print 4

x=int(input("Please enter 1st number: "))
y=int(input("Please enter 2nd number: "))
z=int(input("Please enter 3rd number: "))
print(max(x,y,z), "is the highest number.")