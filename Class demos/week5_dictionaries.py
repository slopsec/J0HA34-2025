# Dictionaries: associating keys with values

student = {
    "name" : "Brooke",
    "occupation": "student",
    "age": 25,
    "subjects": ["cyber," "programming"]
}

# Print description of dictionary
print(student)

# Print selected keys
print(student["name"])
print(student["age"])

# Change a value
student["age"] = 24
print(student["age"])

# Create new entry, just set up
student["truthful"] = False

# Conversion to a list will list the keys
keys = list(student)
print(keys)

# For each key, print value
for k in list(student):
    print(student[k])

# Alternatively, .items() returns all the k:v pairs as tuples
for i in student.items():
    print(i[0], ":", i[1])
