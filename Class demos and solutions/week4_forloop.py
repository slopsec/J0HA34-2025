

# Python for loop
l1 = [1,3,5,6,9]
l2 = ['Mark', 'Lorna', 'Jim', 'Fiona']
l3 = "Kilmarnock"

# print all names in each list
for i in l1:     # i takes value of each element in l1
    print(i)

for j in l2:    # same logic applies
    print(j)

for k in l3:
    print(k)


# Python only has a "foreach" type of loop
# Ranges allow you to create a sequence of integers
# To mimic a for loop based on a counter

# range(start=0, end, step=1)

# Ex. 

# Run 10 times
for i in range(10):
    print(i, "Hello")

print()

# Start from 1 and end at 10 inclusive
for i in range(1, 11):
    print(i, "World")

# Start from 0 and end at 20
# Skip every other
for j in range(0, 21, 2):
    print(j)

for k in range(10, 0, -1):
    print(k)

# E.g. you list a long list of numbers

r = list(range(0, 1000))

print(r)
