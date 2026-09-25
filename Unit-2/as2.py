print('\n===========================================================================================')
print('2.  Write a program to check whether a number is positive negative or zero using nested conditions.')
print('===========================================================================================')

num = int(input("\nEnter a Number : "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

