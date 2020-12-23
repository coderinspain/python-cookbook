#Imports


import mycode as person

#Scope issues
global name # can shove it into the global scope but we should not
# print(name) #not in the same scope
print(person.name)

#Test the code
person.name = 'Mario'
person.greet()
person.toFile('test.txt')

person.name = 'Sofie'
person.greet()

person.fromFile('test.txt')
person.greet()
