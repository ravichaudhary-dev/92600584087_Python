print('\n===========================================================================================')
print('7. Write a program to demonstrate list dictionary and set comprehensions.             ')
print('===========================================================================================')

numbers = [1, 2, 3, 4, 5, 5]

# List comprehension
squares = [x ** 2 for x in numbers]
print("List comprehension:", squares)

# Dictionary comprehension
square_dict = {x: x ** 2 for x in numbers}
print("Dictionary comprehension:", square_dict)

# Set comprehension
square_set = {x ** 2 for x in numbers}
print("Set comprehension:", square_set)