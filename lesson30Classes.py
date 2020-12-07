#Classes

#OOP - object Oriente Programming
#Blue prints for createing objects

# self is the first param
# It is equal to "this" in other languages
# Instance = created

import cat
from cat import Cat

#Use the class
def test():
    b = Cat('Otello', 1, 'Yellow')
    c = Cat('KitKat', 2, 'Tabby')
    print(b)
    print(c)
    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

if __name__ == "__main__":
    x = Cat('linux')
    print(x)
    test()