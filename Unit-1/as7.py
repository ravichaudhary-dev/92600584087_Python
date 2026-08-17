print('\n===========================================================================================')
print('7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.')
print('===========================================================================================')

# Creating a dictionary
student = {
    "name": "Ravi",
    "age": 21,
    "course": "Computer Science",
    "marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))  

# Adding / Updating values
student["marks"] = 90  
student["city"] = "Rajkot" 
print("After update:", student)

# Removing values
student.pop("age")  
print("After pop:", student)

del student["course"]  
print("After delete:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# copy()
copy_dict = student.copy()
print("Copy of dictionary:", copy_dict)

# update()
student.update({"marks": 95, "email": "ravi@example.com"})
print("After update() method:", student)

# clear()
temp = student.copy()
temp.clear()
print("After clear():", temp)

# Iteration over dictionary
print("\nIterating over dictionary:")
for key in student:
    print(key, ":", student[key])

print("\nIterating using items():")
for key, value in student.items():
    print(key, "=>", value)

print('\n===========================================================================================')
