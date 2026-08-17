print('\n===========================================================================================')
print('8. Write a program to explain mutable and immutable objects in Python.')
print('===========================================================================================')

tuple = (10, 20, 30, 40, 50, 60, 70)
print('\nOriginal Tuple ', tuple)

try:
    tuple[0] = 99
except TypeError as e:
    print('tuple can not be modifie - ',e)

list = [10,20,30,40,50,60]
print('\nOriginal List : ',list)

list[0] = 90
print('After modifying list : ',list)

student = {
    'name':'Ravi',
    'marks':55
}
print('\nOriginal Dictonary : ', student)

student['marks'] = 90
print('After Update Dictonary : ',student)

print('\n===========================================================================================')
