class SubjectInterface(object):
    """
    Define the common interface of RealSubject and Proxy so that a Proxy can be
    used anywhere a RealSubject is expected.
    """
    def request(self):
        pass

class Proxy(SubjectInterface):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    
    def __init__(self, real_subject):
        self._real_subject = real_subject
    
    def request(self):
        print('Proxy may be doing something, like controlling request access')
        self._real_subject.request()

class RealSubject(SubjectInterface):
    """
    Define the real object that the proxy represents
    """
    
    def request(self):
        print('The real thing is dealing with the request')
    
if __name__ == '__main__':
    rs = RealSubject()
    rs.request()
    print('='*70)
    proxy = Proxy(rs)
    proxy.request()
