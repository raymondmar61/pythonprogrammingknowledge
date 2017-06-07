#ProgrammingKnowledge 9 Python IF ELSE Statements
#ProgrammingKnowledge 10 Python elif and nested if Statements
#ProgrammingKnowledge 11 Comparison Operators, Logical Operators, is and in

n = int(input("Number? "))

if n < 0:
	print("The absolute value of",n,"is", -n) #integers use , or commas to concatenate
else:
	print("The absolute value of",n,"is", n)
	pass

name = input("Name? ")

if name == "mark":
	print("The name is" ,name) #, or commas work for string, too. No need string space
elif name == "john":
	print("The name is " +name) #+ or plus need string space.
elif name == "july":
	print("The name is " +name)
elif name == "tom":
	print("The name is " +name)
else:
	print(name + " is not on the list")

thing = "animal"	
animalName = "cat"
if thing == "animal":
	if animalName == "dog":
		print("valid animal Name dog") #nestedif prints only animalName is "dog"
	else:
		print("invalid animal Name")
	print("thing is animal")
else:
	print("the thing is invalid")

if 9 > 10 and 9!= 10:
	print("and True")
else:
	print("and False")

if 9 > 10 or 9!= 10:
	print("or True")
else:
	print("or False")

string = "abcde"
if "abc" in string: #result is yes
	print("yes")
else:
	print("no")

a = [1,2,3]
if 3 in a:
	print("True")  #print True
else:
	print("False")