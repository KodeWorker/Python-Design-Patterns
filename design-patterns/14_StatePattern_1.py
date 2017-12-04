# Base state class

class ComputerState(object):
    name = 'state'
    allowed = []
    
    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current: %s -> switched to new state %s' %(self, state.name))
            self.__class__ = state
        else:
            print('Current: %s -> switched to new state %s not possible.'
                  %(self, state.name))
    
    def __str__(self):
        return self.name

class Off(ComputerState):
    name = 'off'
    allowed = ['on']

class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']

class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']

class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']

class Computer(object):
    def __init__(self):
        self.state = Off()
        
    def change(self, state):
        self.state.switch(state)

if __name__ == '__main__':
    
    c = Computer()
    c.change(On)
    
    c.change(Suspend)
    c.change(Hibernate)
    
    c.change(On)
    c.change(Off)
    