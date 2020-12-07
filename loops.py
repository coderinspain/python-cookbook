# Loops

#While loop
x = 0
while x < 10:
    x += 1
    print(f'x = {x}')
print('Test 1 is done!')

#Pass
# be careful with pass in a while loop. It will loop for ever

#Continue and break
x = 0
while True:
    x += 1
    if x < 5:
        print(f'x  < 5 {x}')
        continue
    print(f'Do something {x}')

    if x == 10:
        print(f'Exiting x = {x}')
        break
print('Complete')


#For loop on dictionaries
x = dict(Bryan=46, Tammy=48, Heather=28, Chris=30)
print(x)

for k in x.keys():
    print(f'Kyes: {k} = {x[k]}')

for k,v in x.items(): #This is a better way to loop in a dictionary!!!!
    print(f'Items: {k} = {v}') 


def greet(name):
    print(f'Hello {name} great progress')
#Range
x = range(10)
print(x)
for i in x:
    greet('Mario') #You can print a function by calling it direct
    # print(f'Range: {i}')

#Range start, stop and step
x = range(5, 21, 3)
print(x)
for i in x:
    print(f'Stepped: {i}')









