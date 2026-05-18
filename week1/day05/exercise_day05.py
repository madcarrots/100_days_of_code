# Thomas Zermeno
# May 17, 2026
# Day 05 Exercises
# 100 Days of Python

# Exercise 1
# Tuple basics
print("----Day 05----")
dimensions = (1920, 1080)
print("\nWidth: \t", dimensions[0])
print("height: ", dimensions[1])
# dimensions[0] = 4200
# TypeError: 'tuple' object does not support item assignment

# Exercise 2
# Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\n")

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

set1.add(69)
print(set1)


# Exercise 3
# Dictionary Lookup

# create a dictionary
student = {"name": "John", "grade": "A", "age": 16}
print("Name: ", student["name"], "\tAge:", student["age"])
print("Email:", student.get("email"))