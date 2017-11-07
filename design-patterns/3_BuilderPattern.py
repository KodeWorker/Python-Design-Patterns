###############################################################################
# 1. Product: contains different parts
# 2. Director: returns assembled object
# 3. Builder: returns different product parts
# Flow:
#           Director ---> [Abstract Builder] <--- Concrete Builder #2 
#                               ^                           ^
#                               |                           |
#                       Concrete Builder #1                 |
#                               ^                           |
#                               |                       Product #2
#                           Product #1
###############################################################################

# Product
class Plane(object):
    def __init__(self):
        self.__wings = list()
        self.__wheels = list()
        self.__engine = None
        self.__body = None
    
    def attachWing(self, wing):
        self.__wings.append(wing)
    
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)
    
    def setEngine(self, engine):
        self.__engine = engine
    
    def setBody(self, body):
        self.__body = body
    
    def specification(self):
        print('body: %s' %self.__body.shape)
        print('engine hoorsepower: %d' %self.__engine.horsepower)
        print('wing length: %d ft.' %self.__wings[0].length)
        print('tire size: %d in.' %self.__wheels[0].size)

# Product parts
class Wing(object):
    length = None
    
class Wheel(object):
    size = None

class Engine(object):
    horsepower = None

class Body(object):
    shape = None

# Director
class Director(object):
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
    
    # code for assembling a plane
    def getPlane(self):
        plane = Plane()
        
        body = self.__builder.getBody()
        plane.setBody(body)
        
        engine = self.__builder.getEngine()
        plane.setEngine(engine)
        
        i = 0
        while i < 2:
            wing = self.__builder.getWing()
            plane.attachWing(wing)
            i += 1
        
        j = 0
        while j < 4:
            wheel = self.__builder.getWheel()
            plane.attachWheel(wheel)
            j += 1
                
        return plane

# Builder Interface
class PlaneBuilderInterface(object):
    def getBody(self): pass
    def getEngine(self): pass
    def getWing(self): pass
    def getWheel(self): pass

class b747Builder(PlaneBuilderInterface):
    def getBody(self):
        body = Body()
        body.shape = 'type-747'
        return body
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100000
        return engine
    
    def getWing(self):
        wing = Wing()
        wing.length = 231
        return wing
    
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 49
        return wheel

class b787Builder(PlaneBuilderInterface):
    def getBody(self):
        body = Body()
        body.shape = 'type-787'
        return body
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 120000
        return engine
    
    def getWing(self):
        wing = Wing()
        wing.length = 197
        return wing
    
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 50
        return wheel

if __name__ == '__main__':
    
    director = Director()
    print('='*40)
    director.setBuilder(b747Builder())
    plane1 = director.getPlane()    
    plane1.specification()
    print('='*40)
    director.setBuilder(b787Builder())
    plane2 = director.getPlane()    
    plane2.specification()
    print('='*40)