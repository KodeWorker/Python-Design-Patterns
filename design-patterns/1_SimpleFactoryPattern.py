###############################################################################
# 1. ObjectInterface: common interface for genereated objects
# 2. FactoryObject: returns object
#
# Flow:
#           client ---> [Factory ---> Abstract] <--- [Object1, Object2, ...]
#               ^                         |
#               |                         |
#               ---------------------------
#
#
###############################################################################
# Example: Animal Farm Factory

## Object Code
# 1. ObjectInterface
class Animal(object):
    def voice(self):
        pass

class Pig(Animal):
    def voice(self):
        print('Oink')

class Cow(Animal):
    def voice(self):
        print('Moo')
        
class Duck(Animal):
    def voice(self):
        print('Quack')

## Factory Code
# 2. FactoryObject
class AnimalFarmFactory(object):
    
    @staticmethod
    def getAnimal(name):
        if name == 'Duck':
            return Duck()
        elif name == 'Cow':
            return Cow()
        elif name == 'Pig':
            return Pig()
        else:
            assert 0, 'Could not find animal "%s"' %name

## Client Code

if __name__ == '__main__':
    
    # Create animal "Pig"
    f = AnimalFarmFactory()
    animal = f.getAnimal('Pig')
    animal.voice()
    
    # Create animal "Cow"
    animal = f.getAnimal('Cow')
    animal.voice()
    
    # Create animal "Duck"
    animal = f.getAnimal('Duck')
    animal.voice()
    
    # What about animal "Goat"?
    animal = f.getAnimal('Goat')
    animal.voice()