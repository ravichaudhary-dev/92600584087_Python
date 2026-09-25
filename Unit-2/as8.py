print('\n===========================================================================================')
print('8. Write a program to illustrate variable scope using local global and nonlocal variables.   ')
print('===========================================================================================')

x = 10

def local():
    y = 20

    def inner():
        local_value = 5

        global x
        nonlocal y

        x = x + 1
        y = y + 1

        print("local:",local_value)
        print("Global;",x)
        print("Nonlocal:",y)
    inner()
local()


print("Global outside function:",x)