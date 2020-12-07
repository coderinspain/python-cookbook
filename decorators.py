#Decorators

#Everythin in Python is an object
#That means functions can be used as objects
#So we can do some really cool thins
#A decorator takes in a function, adds som functionality and returns it.

#Decorator with params
#This has a defined number of params

def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Can not divide by zero')
                return False
            return True
        print(f'{o} is not a number')
        return False
    
    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x,y)
    return inner

@numcheck
def divide(a, b):
    print(a / b)

divide(100, 3)
divide(100, 0)
divide(100, 'horse')

#Decorator with unknown number of params
#We want a decorator that can pass params and handle anything
#We aslo want to chain them together
# *args, ** kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args, **kwargs)
        print('~'*20)
    return inner

def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg={x}')

        for k,v in kwargs.items():
            print(f'key={k}, value={v}')

    return inner

@outline
@list_items
def display(msg):
    print(msg)
    

display('Hello world')

@outline
@list_items
def birthday(name='', age=0):
    print(f'Happy birthday {name} you are {age} years old')


birthday(name='Mario', age=47)




