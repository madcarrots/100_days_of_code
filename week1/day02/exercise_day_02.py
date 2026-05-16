# thomas zermeno
# exercise_day_2.py
# May 15, 2026

#Exercise 1: Swap Two Variables
# Write a Python program that swaps the values of two variables.

print("----Exercise 1----")
a = 5
b = 17
print("a = ", a)
print("b = ", b)
swap = a
a = b
b = swap
print("\n~Presto!~ \n~Change-o!~\n")
print(f"a = {a}")
print(f"b = {b}")
print("\nHold your applause!\nNo, no! I mean it....")

# Exercise 2: Simple calculator
# Create variables x and y, assign any two numbers and print their
# -Addition
# -Subtraction
# -Multiplication
# -Division

print("\n\n----Exercise 2----")

#create values
x = 17
y = 11

#create calculations
add = x + y
sub = x - y
times = x * y
div = x / y

# output
print(f"x = {x}")
print(f"y = {y}")
print(f"Addition: \t{add}")
print(f"Subtraction: \t{sub}")
print(f"Multiplication: {times}")
print(f"Division: \t{div}")


# Exercise 3: Type Identification
# Create one variable of each of the following data types and print their type

print("\n\n----Exercise 3----")
print("-Integer\nx = 3")
x = 3
print(type(x))
print("\n-Float\ny = 3.14159")
y = 3.14159
print(type(y))
print("\n-String\nz = \"This is a string\"")
z = "This is not a string."
print(type(z))
print("\n-Boolean\naa = true")
aa = True
print(type(aa))

# Bonus Exercise
# Temperature Coverter

print("\n\n----BONUS Question----")
cel = 18
far = (cel * 9/5) + 32
print(f"{cel} Degrees Celsius to Fahrenheit")
print(f"\nCelsius: {cel} --> Fahrenheit: {far}")
