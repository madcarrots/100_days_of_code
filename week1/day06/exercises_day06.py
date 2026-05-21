# Thomas Zermeno
# May 18, 2026
# Day 06 Exercises
# 100 Days of Python

# Day06 Exercises
# Exercise 1
# Simple type casting

num_str = input("Please enter a number: \t")
num_int = int(num_str)
result = num_int + 10
print(f"The result is: {result}")
print("Double the result is:", result * 2)

# Exercise 2
# Float to Int

price_str = float(input("\nEnter price: \t"))
price_int = int(price_str)
print(f"You provided {price_str}.  Converted to an integer that is {price_int}.")

# Exercise 3
# Use f-strings

print("")
name_str = input("Please enter your name: ")
age_str = input("Please enter your age: \t")

print(f"\nHi, {name_str}, you are {age_str} years old!")


# Bonus Exercise
# Tax Calculator

price_float = float(input("\nEnter price: \t"))
price_str = str(price_float)

tax_float = float(input("\nEnter tax %: \t"))
tax_str = str(tax_float)
tax_amount = tax_float * price_float / 100
total = tax_amount + price_float

print("")
print(f"A product that costs ${price_float} with {tax_str}% tax will have a total price of ${total:.2f}.")