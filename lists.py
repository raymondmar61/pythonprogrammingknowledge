#ProgrammingKnowledge 7 Python Lists
#ProgrammingKnowledge 8 Python Slices or Slicing

names = ["mark","john","july"]
print(names) #print ["mark","john","july"]
print(names[0]) #print mark
print(names[2]) #print july
print("There's not such thing as -0 or negative zero index number.")
print(names[-1]) #print july
print(names[-3]) #print mark

names.append("patrik")
print(names) #print ['mark', 'john', 'july', 'patrik']

age = [23, 12, 32, 11]
names.extend(age)
print(names) #print ["mark","john","july","patrik", 23, 12, 32, 11]

names.remove("patrik")
print(names) #print ["mark","john","july", 23, 12, 32, 11]
print(len(names)) #print 7
print("\n")

mylist = [0,1,2,3,4,5,6,7,8,9]
print(mylist)
print(mylist[:]) #print [0,1,2,3,4,5,6,7,8,9], syntax useful in loops
print(mylist[4:]) #print [4, 5, 6, 7, 8, 9]
print(mylist[4:8]) #print [4, 5, 6, 7]
print(mylist[4:9]) #print [4, 5, 6, 7, 8]
print("Always add +1 to the right side of the :")
print(mylist[:10]) #print [0,1,2,3,4,5,6,7,8,9], syntax useful in loops
print(mylist[-1:-6:-1]) #print [9, 8, 7, 6, 5]
print(mylist[-6:-1]) #print [4, 5, 6, 7, 8]
print(mylist[-6:]) #print [4, 5, 6, 7, 8, 9]
print(mylist[0:10:2]) #print [0, 2, 4, 6, 8]
print(mylist[2:8:2]) #print [2, 4, 6]
print(mylist[::+3]) #print [0, 3, 6, 9]
print(mylist[::-3]) #print [9, 6, 3, 0]