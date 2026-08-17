print('\n===========================================================================================')
print('6. Write a program to illustrate the use of tuples and sets with basic operations.')
print('===========================================================================================')

'''
6. Write a program to illustrate the use of tuples 
and sets with basic operations. 
'''

print("=============== Tuple Example ===============")

tuple = (10, 20, 30, 40, 50 ,100, 80,)

print("\nTuple:", tuple)
print("First element:", tuple[0])
print("Last element:", tuple[-1])
print("Slice (index 1 to 3):", tuple[1:4])
print("Length of tuple:", len(tuple))
print("Count of 20:", tuple.count(20))
print("Index of 30:", tuple.index(30))



print("\n=============== Set Example ===============")

set = {10, 20, 30, 40, 50, 20}  

print("\nSet:", set)

set.add(60)
print("After adding 60:", set)

set.remove(30)
print("After removing 30:", set)


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)

print('\n===========================================================================================')