# In Python string are built-in
# By default all single character variables are strings

string1 = "Today is Tuesday."
string2 = "Python is a programming language."
string3 = "It was designed in the 1990s."

# Combine strings = concatenation
# + -> concatenating strings

string4 = string1+ " " + string2+string3
print(string4)

# string5 = string4 + 23 will fail, type cast
string5 = string4 + str(23)  
print(string5)

# Strings are sequential like lists and Python allows manipulation
# With the same tools as lists

# Ex 1 -> foreach loop
for c in "Hello":
    print(c)

# Ex 2 -> len and slicing
# "Today is Tuesday"

# string[start:end:stride]
print(string1, "has", len(string1), "characters")
substring = string1[3:len(string1)//2+3]
print(substring)

substring = string1[len(string1)//2:0:-1]
print(substring)

# Reversing a string is straightforward
print(string1[::-1])