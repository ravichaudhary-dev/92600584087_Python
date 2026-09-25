print('\n===========================================================================================')
print('4. Write a program to find the sum of digits of a number using a while loop.             ')
print('===========================================================================================')

# while Loop
num = int(input("Enter a Number : "))

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum of digits =",total)