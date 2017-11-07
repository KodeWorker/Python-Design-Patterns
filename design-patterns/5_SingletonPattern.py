class Singleton(object):
    __instance = None
    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance

if __name__ == '__main__':
    x = Singleton()
    x.val = 'burger'
    print('x.val = %s ' %x.val)
    
    y = Singleton() # <--- return and "init"(__instance = None) the same object from x
    y.val = 'chip'
    print('y.val = %s' %y.val)
    
    print('What about x.val now? -> %s' %x.val)
    
    print('If x and y are the same object? -> %s' %(x == y))