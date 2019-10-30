class Animal:
    planet = 'Earth'

    def __init__(self, animal_type, legs, can_speak):
        self.name = ''
        self.animal_type = animal_type
        self.legs = legs
        self.can_speak = can_speak

    def give_name(self, name):
        self.name = name

class Man(Animal):
    is_hero = False

    def __init__(self, can_drive, is_employed):
        Animal.__init__(self, 'Homosapien', 2, True)

        self.can_drive = can_drive
        self.is_employed = is_employed

    def say_name(self):
        print('Hey, I am {}'.format(self.name))

class SuperHuman(Man):
    def __init__(self, power, is_hero):
        Man.__init__(self, True, True)
        self.alias = ''
        self.power = power
        self.is_hero = is_hero

    def set_alias(self, name):
        self.alias = name

    def show_power(self):
        print('Okay, Now I will do {}'.format(self.power))

    def say_dialogue(self):
        print('Yo! I am {}, I will kill you!'.format(self.alias))


dino = Animal('Dinosaur', 4, False)
dino.give_name('Archie')

print(dino.legs)

soni = Man(True, True)
soni.give_name('Bharat')

print(soni.legs)
soni.say_name()

gangadhar = SuperHuman('fly', True)
gangadhar.set_alias('Shaktimaan')

gangadhar.say_dialogue()

