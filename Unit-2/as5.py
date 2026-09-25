print('\n===========================================================================================')
print('5. Write a program to demonstrate the use of break continue and pass statements.             ')
print('===========================================================================================')

marks = [45, 78, 0, 65, 92, -1, 34]

for mark in marks:

    if mark == 0:
        continue

    elif mark < 0:
        break

    elif mark <= 50:
        pass

    else:
        print("Good marks:", mark)