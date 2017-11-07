class Borg(object):
    __shared_state = {}
    def __init__(self):
        # we can access the attribute via self.__dict__
        self.__dict__ = self.__shared_state

if __name__ == '__main__':
    b1 = Borg()
    b2 = Borg()
    
    print('If b1 and b2 are the same object? -> %s' %(b1 == b2))
    
    b1.val = 'milkshake'
    
    print('Set b1.val to "milkshake", and then b2.val becomes: %s' %b2.val)
