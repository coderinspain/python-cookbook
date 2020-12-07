# Create the class

class Cat:
    name = ''
    age = 0
    color = ''

    def __init__(self, name, age= 1, color='white'): #self is required, the other parameters are optional
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    
    def meow(self):
        print(f'{self.name} meow')

    
    def sleep(self):
        print(f'{self.name} zzzzz')


    def hungry(self):
        for x in range(5):
            self.meow()

    def eat(self):
        print(f'{self.name} nom nom nom')


    def description(self):
        print(f'{self.name} is a {self.color} cat, who is  {self.age} years old')



    
