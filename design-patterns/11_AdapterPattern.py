# Adaptee (source) interface

class EuropeanSocketInterface(object):
    def voltage(self):
        pass
    def live(self):
        pass
    def neutral(self):
        pass
    def earth(self):
        pass

# Target interface
class USASocketInterface(object):
    def voltage(self):
        pass
    def live(self):
        pass
    def neutral(self):
        pass

# Adaptee
class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230
    def live(self):
        return 1
    def neutral(self):
        return -1

# client
class AmericanKattle(object):
    __power = None
    
    def __init__(self, power):
        self.__power = power
    
    def boil(self):
        if self.__power.voltage() > 110:
            print('Kattle is on fire!')
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print('Coffee time!')
            else:
                print('No power!')

# Adapter
class Adapter(USASocketInterface):
    __socket = None
    
    def __init__(self, socket):
        self.__socket = socket
    
    def voltage(self):
        return 110
    
    def live(self):
        return self.__socket.live()
    
    def neutral(self):
        return self.__socket.neutral()

if __name__ == '__main__':
    Esocket = EuropeanSocket()
    Akettle = AmericanKattle(Esocket)
    Akettle.boil()
    
    Akettle2 = AmericanKattle(Adapter(Esocket))
    Akettle2.boil()
    