#Test class


class Person:
    #Weak Private
    _name = 'No Name'
    def setName(self, name):
        self._name = name
        print(f'Name set to {self._name}')
    
    #String Private
    def __think(self):
        print('Thinking of my self')

    def work(self):
        self.__think()

    #Before and After
    def __init__(self):
        print('Constructor')

    def __call__(self):
        print('Call someone')


class Child(Person):
    def testDouble(self):
        self.__think(self)
