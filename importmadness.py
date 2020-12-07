# Import maddness

#__init__
# what is it, why do we need it

#make a sub folder
#add the files / code

#Imports
from sub import * #careful with this, this will import everything. 
from sub import test as code

#Call the code
def main():
    print('This is the main function')
    greet()
    code.greet()

if __name__ == "__main__":
    main()


