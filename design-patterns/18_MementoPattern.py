import copy

class Memento(object):
    
    def __init__(self, data):
        # make a deep copy of every variables in the given class
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))

class Undoable(object):
    
    def __init__(self):
        # each instance keeps the latest saved copy so that there is only one
        # copy of each memory
        self.__last = None
    
    def save(self):
        self.__last = Memento(self)
    
    def undo(self):
        for attribute in vars(self):
            setattr(self, attribute, getattr(self.__last, attribute))

class Data(Undoable):
    
    def __init__(self):
        super(Data, self).__init__()
        self.numbers = []

if __name__ == '__main__':
    d = Data()
    repeat = 10
    for i in range(repeat):
        d.save()
        d.numbers.append(i)    
    d.save()
    
    for _ in range(repeat):
        d.undo()
        print(d.numbers)
    