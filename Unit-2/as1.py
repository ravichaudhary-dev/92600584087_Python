print('\n===========================================================================================')
print('1. Write a program to demonstrate conditional statements using if if-else and if-elif-else.  ')
print('===========================================================================================')

# if

print("\n---Voting Eligibility Check---")

age = int(input("Enter your age : "))

if age >= 18 :
    print("You are Eligible for Vote.")

# if else

print("\n---Odd or Even Check---")

num = int(input("\nEnter a Number : "))

if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

# if elif else

print("\n---Electricity Bill Consumption---")

unit = int(input("\nEnter Your Electricity Bill Unit : "))

if unit <= 100:
    print("Low Consumption.")
elif unit <=300:
    print("Medium Consumption.")
elif unit <= 500:
    print("High Consumption.")
else:
    print("Very High Consumption.")



