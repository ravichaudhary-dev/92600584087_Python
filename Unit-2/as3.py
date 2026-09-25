print('\n===========================================================================================')
print('3. Write a program to generate a multiplication table using a for loop. ')
print('===========================================================================================')

num = int(input("\nEnter a Number : "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")