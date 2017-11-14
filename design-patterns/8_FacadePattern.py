class Engine(object):
    
    def __init__(self):
        self.spin = 0
        
    def start(self, spin):
        self.spin = min(spin, 3000)

class StarterMoter(object):
    
    def __init__(self):
        self.spin = 0
    
    def start(self, charge):
        if charge > 50:
            self.spin = 2500

class Battery(object):
    def __init__(self):
        self.charge = 0

class Car(object):
    
    def __init__(self):
        self.engine = Engine()        
        self.starter = StarterMoter()
        self.battery = Battery()
        
    def turn_key(self):
        self.starter.start(self.battery.charge)
        self.battery.charge -= 50
        self.engine.start(self.starter.spin)
        if (self.engine.spin > 0):
            print('Engine started')
        else:
            print('Engine not started')
    
    def jump(self):
        self.battery.charge = 100
        print('Jumped')

if __name__ == '__main__':
    c = Car()
    c.turn_key()
    print(c.battery.charge)
    c.jump()
    print(c.battery.charge)
    c.turn_key()
    print(c.battery.charge)