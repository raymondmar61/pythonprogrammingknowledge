#ProgrammingKnowledge 6 Strings

b = "I am a double quoted string, ain\"t single quoted string allowed using \\ backslash character called escape character."
c = "Hello "
d = 5
e = (len(b))

print(b) #print I am a double quoted string, ain"t single quoted string allowed using \ backslash character called escape character.
print(len(b)) #print 116
print("The length is", len(b)) #print The length is 116
print("The length is", e) #print The length is 116
print(c*10) #print Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello 
print(c + str(d)) #print Hello 5, concatenate Hello string and 5 converted to string