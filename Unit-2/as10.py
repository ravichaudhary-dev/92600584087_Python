print('\n===========================================================================================')
print('10. .Write a program to generate a sequence of numbers using generator functions and yield keyword.')
print('===========================================================================================')

def generate_numbers():
    for number in range(1, 6):
        yield number

for value in generate_numbers():
    print(value)