# Thomas Zermeno
# May 29, 2026
# Day 07 Project
# 100 Days of Python

# Welcome customer
print("Welcome Customer!\nPlease provide us with some basic information about yourself.")
name_str = input("What is your name? : \t\t")
age_int = int(input("How old are you? : \t\t"))
city_str = input("What city do you live in? : \t")
fave_lang = input("What is your favorite programming language? : ")
hobby_input = input("Enter your 3 favorite hobbies, separated by a comma: ")
hobby_list = hobby_input.split(",")
hobbies = []
hobby1 = input("What is your favorite hobby? : \t\t")
hobbies.append(hobby1)
hobby2 = input("What other hobby do you enjoy? : \t")
hobby3 = input("What's one more hobby that you have? : \t")
hobbies.append(hobby2)
hobbies.append(hobby3)

print("\n\n********** Info Card **********")
print(f" Name: {name_str} ")
print(f" Age: \t{age_int}")
print(f" Metro: {city_str}")

print("\n Interests")
print(f" 1) \t\t{hobbies[0]}")
print(f" 2) \t\t{hobbies[1]}")
print(f" 3) \t\t{hobbies[2]}")