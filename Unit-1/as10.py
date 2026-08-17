print('\n===========================================================================================')
print('10.Write a program to demonstrate recursion using factorial or Fibonacci series.')
print('===========================================================================================')

#  Factorial number using recursion
def factorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * factorial(n - 1) 

num = 5
print(f'Fectotial number of {num} = ',factorial(num))

# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:  
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = 10
print(f'First {terms} terms of Fibonacci series: ')
for i in range(terms):
    print(fibonacci(i), end=' ')

print('\n===========================================================================================')
