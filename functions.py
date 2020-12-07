# def test():
#     print('This is a function')

# #Define a funciton with parameters and return a value
# def sqft(w,h):
#     v = w * h
#     return v


#Call a function
# test()

#Call a function multiple times
# for x in range(4):
#     test()

#Call a function with parameters

# x = sqft(3,4)
# print(f'The square footage is {x}') # when passing arguments you have to assigned to a variable!!!

#Functions and scope

#Is a convention used with many programming languages that sets the scope
#(range of functionality) of a variable so that it may only be called
#from within the block of code in which it is defined.
#Scopes can be nested inside another.

#This is the global scope
name = 'Mario Ibarra'

# def test1():
#     print(f'My name is {name}')

# test1()

#Global scope can not access function scope
x = 10
def test2():
    x = 50
    print(f'Function scope {x}')

test2()
print(f'Global scope {x}')


#Functions can return values
def numbers(steps):
    l = range(1, 21, steps)
    for i in l:
        print(i)
    return l

def lotto():
    z = numbers(3)
    for x in z:
        print(f'Lucky number {x}')

lotto()
















