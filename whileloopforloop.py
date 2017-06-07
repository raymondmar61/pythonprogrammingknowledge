#ProgrammingKnowledge 12 While Loop and For Loops

a = 0 #initialize while loop
while a < 5:
	print(a)
	a+=1 #a = a + 1
	pass

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

c = [3, 4, 5, 2, 3, 7, 6, 5, 4, 3, 2]
for eachc in c:
	print(eachc) #prints each number c in the list c in its own line
	pass