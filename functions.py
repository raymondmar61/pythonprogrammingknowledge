#ProgrammingKnowledge 13 Defining Functions
#ProgrammingKnowledge 14 Default parameters and Multiple Arguments in Python
#A function is a group of statements performing a specific task
# def functionname(arg1, arg2, arg3, ...):
# 	statement1
# 	statement2
# 	...

def hello(name):
	print("Hello " +name)
	pass
hello("Mark") #return Hello Mark

def add(x,y):
	return (x+y)
print(add(3,5)) #prints 8
print(add(234,333)) #prints 567
sum = add(100, 500)
print(sum) #prints 600

def studentScore(name, score):
	print(name+ " scored" ,score) #score is an integer
	print(name+ " scored " +str(score)) #alternatively
studentScore("Mark",70) #return Mark scored 70 *new line* Mark scored 70

#we can initialize or set a default in a function
def studentScoreInitialize(name="Top", score = 80):
	print(name+ " scored" ,score) #score is an integer
studentScoreInitialize() #return Top scored 80, the default values
	
#if a function does have a value, default is removed in a function
def studentScoreInitializeNoDefault(name="Tom", score=80):
	score = str(score) #score is an integer.  Convert to string.
	print(name+ " scored " +score) 
studentScoreInitializeNoDefault("NoDefault",50) #return NoDefault scored 50.  BTW, default score is 80 if studentScoreInitializeNoDefault("June").  Also studentScoreInitializeNoDefault(score=99) returns "Tom scored 99"
studentScoreInitializeNoDefault("June") #return June scored 80 
studentScoreInitializeNoDefault(score=99) #return Tom scored 99

#multiple passes in one variable
def studentScores(name, *scores):
	print(name)
	print(scores)
studentScores("Mark",55,77,90,67) #return Mark *new line* (55,77,90,67)