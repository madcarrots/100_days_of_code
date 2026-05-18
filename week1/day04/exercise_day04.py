# Thomas Zermeno
# May 17, 2026
# Day 04 Exercises
# 100 Days of Python


# Exercise 1
# Your favorite things

favorites = ["watermelon", 
             "roller skates",
             "Angine de Poitrine",
             "pepperoni pizza",
             "zombie games"]

print(f"Favorite thing #1 : \t{favorites[0]}")
print(f"Favorite thing #5 : \t{favorites[-1]}")
print(f"Favorite thing #3 : \t{favorites[2]}")


# Exercise 2
# List slicing and length

cities = ["Montreal", "Toronto", "Vancouver", "Calgary", "Ottawa"]

print("The first three cities are: " + str(cities[0:3]))
print("The last two cities are: " + str(cities[-2]))  # can use negative count
print("The total number of cities is: " + str(len(cities))) # adding a string is arduous

print("A better way to list the cities: ", cities[1:4])
print("Well, there are", len(cities),"of them.") # extra spaces not required with comma


# Exercise 3
# Modify and sort a list

numbers = [42, 7, 13, 99, 5]
numbers.append(25)
numbers.remove(13)
numbers.sort()
print(numbers)