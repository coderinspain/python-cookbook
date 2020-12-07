# The underscore

#Often ignored, multiple uses
# _Single
#__Double
#__Before
#After__
#__Both__

#Skipping
for _ in range(4): # Python ignore the underscore and run the code anyway. You can use also x and the program does not complain
    print('Hello') 


#Test class
from person import *

#Before (Single)
#Internal use only, internal to is class or scope. (called a weak private)
p = Person()
p.setName('Mario')
print(f'Weak private {p._name}')
p._name = 'Nooooooooo'
print(f'Weak private {p._name}') # You must never change the weak private, you can have a lots of problems!!!


#Before (Double)
#Internal use only, avoid conflict in subclass
# The double underscore is to make private and only to that class it is declered!!!
#and tells python to rewrite the name (Mangling)
p = Person()
p.work()
# p.__think()
# c = Child()
# c.testDouble()

#=======#
#After (Any)
#Helps to avoid naming conflicts with key words
class_ = Person()
print(class_)

#Before and after
#Considered special to Python, like the init and main function
p = Person()
p.__call__()






