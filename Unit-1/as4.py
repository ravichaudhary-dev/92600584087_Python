print('\n===========================================================================================')
print('4. Write a program to demonstrate string operations including slicing formatting and built-in string functions.')
print('===========================================================================================')

# string
text = "Hello Python Programming"

print("Original String      :", text)

# string slicing
print("First 5 characters   :", text[:5])
print("Last 5 characters    :", text[-5:])
print("Characters from index 6 to 12:", text[6:13])
print("Reverse string       :", text[::-1])

name = "Ravi"
age = 24

print('My name is',name,'and I am',age,'year old.')

line = "  My name is Ravi and i am 24 year old.  "
print('Uppercase        :',line.upper())
print('Lowercase        :',line.lower())
print('Title Case       :',line.title())
print('Strip spaces     :',line.strip())
print('Replace          :',line.replace('My', 'Your'))
print('Split            :',line.split())
print("Find 'ravi'      :",line.find('ravi'))
print("Count 'a'        :",line.count('a'))

print('\n===========================================================================================')
