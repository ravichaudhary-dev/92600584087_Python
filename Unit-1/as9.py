print('\n===========================================================================================')
print('9. Write a program to define and use user-defined functions with different types of arguments.')
print('===========================================================================================')
# sum
def add(a, b):
    return a + b

print("\nSum of 10 and 20 =", add(10, 20))

# greeting
def greet(name, msg="Welcome to Python!"):
    return f"Hello {name}, {msg}"

print(greet("Ravi"))
print(greet("Ravi", "Good Evening!"))

def student_info(name, age):
    return f"Name: {name}, Age: {age}"

print(student_info(age=21, name="Ravi"))

def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

print("Multiplication of 2, 3, 4 =", multiply(2, 3, 4))

print('\n===========================================================================================')
