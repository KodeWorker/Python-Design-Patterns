class Observerable(object):
    
    def __init__(self):
        self.observers = []
    
    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def unregister_all(self):
        if self.observers:
            del self.observers[:]
            
    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

# abstract observer class
class Observer(object):
    
    def update(self, *args, **kwargs):
        pass

# concrete observer subclasses
class AmericanStockMarcket(Observer):
    def update(self, *args, **kwargs):
        print('American stock market received: {0}\n{1}'.format(args, kwargs))

class EuropeanStockMarcket(Observer):
    def update(self, *args, **kwargs):
        print('European stock market received: {0}\n{1}'.format(args, kwargs))

if __name__ == '__main__':
    really_big_company = Observerable()
    american_observer = AmericanStockMarcket()
    european_observer = EuropeanStockMarcket()
    
    really_big_company.register(american_observer)
    really_big_company.register(european_observer)
    really_big_company.update_observers('important_update', msg='CEO unexpectedly resigns')