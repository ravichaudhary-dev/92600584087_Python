print('\n====================================================================')
print('9. Write a program to demonstrate iterators and iterables in Python.  ')
print('====================================================================')

numbers = [10, 20, 30]   # iterable

iterator = iter(numbers)  # iterator

print("Iterable:", numbers)

print("First value:", next(iterator))
print("Second value:", next(iterator))
print("Third value:", next(iterator))