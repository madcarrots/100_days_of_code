# Thomas Zermeno
# May 29, 2026
# Day 07 Project
# 100 Days of Python

# Welcome customer
print("Welcome Customer!\nPlease provide us with some basic information about yourself.")
name_str = input("What is your name? : \t")
age_int = int(input("How old are you? : \t"))
city_str = input("What city do you live in? : ")
fave_lang = input("What is your favorite programming language? : ")
hobby_input = input("Enter your 3 favorite hobbies, separated by a comma: ")
hobby_list = hobby_input.split(",")
hobbies = []
hobby1 = input("What is your favorite hobby? : \t")
hobbies.append(hobby1)
hobby2 = input("What other hobby do you enjoy? : \t")
hobby3 = input("What's one more hobby that you have? : ")
hobbies.extend(hobby2, hobby3)

