print('\n===========================================================================================')
print('6. Write a program to iterate over lists strings and dictionaries using loops.            ')
print('===========================================================================================')

# List
numbers = [10, 20, 30]
print("\nList:")
for num in numbers:
    print(num)

# String
text = "Python"
print("\nString:")
for char in text:
    print(char)

# Dictionary
students = {
    "Ravi": 22,
    "Arjun": 18,
    "Raj": 20
}

print("\nDictionary:")
for name, age in students.items():
    print("Name:", name, "Age:", age)
