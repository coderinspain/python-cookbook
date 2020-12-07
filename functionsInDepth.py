# functions in depth

# #No Arguments
# def test():
#     print('Normal functions')

# print('\r\n------No Arguments')
# test()

# * args -Positional 
def multiple(*args):
    z = 1
    for num in args:
        print(f'Num = {num}')
        z *= num
    print(f'Multiply: {z}')
print('\r\n------*args')
multiple(1, 2, 4, 5, 7, 8, 10)

# **kwargs is used to pass a keyworde, variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display('name')
    display('age')
    display('pet')
    display('paesaeste')

print('\r\n-----**kwargs')
profile(name='Mario', age=46)
profile(name='Mario', age=46, pet='Cat')
profile(name='Mario', age=46, pet='Cat', food='pizza')


#Lambda function (anonymous functions)
print('\r\n-----Lambda')
#normal
def makesqft(width=0, height=0):
    return width * height
print(makesqft(width=10, height=8))
print(makesqft(15,8))

#Lambda
#z = lambda x: x * y
sqft = lambda width=0, height=0: width * height
print(sqft(width=10, height=8))
print(sqft(15,8))


#Packing and unpacking data

# Problem with  *args and **kwarg is we can not use list and dictionaries
#Insted we have to pack and unpack data

#Packing data
def pack(*nums):
    pass













