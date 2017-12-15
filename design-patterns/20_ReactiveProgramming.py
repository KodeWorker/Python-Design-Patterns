from rx import Observer, Observable

class MyObserver(Observer):
    
    def on_next(self, x):
        print("Got: %s" %x)
    
    def on_error(self, e):
        print("Got error: %s" %e)
    
    def on_completed(self):
        print("Sequence completed")

if __name__ == '__main__':
    xs = Observable.from_iterable(range(10))
    d = xs.subscribe(MyObserver())    
    print('-'*20 + '[SUB TO FUNCTION]' + '-'*20)
    xs = Observable.from_(range(10))
    d = xs.subscribe(print)
    print('-'*20 + '[FILTER]' + '-'*20)
    xs = Observable.from_(range(10))
    d = xs.filter(lambda x: x%2).subscribe(print)
    print('-'*20 + '[TRANSFORM]' + '-'*20)
    xs = Observable.from_(range(10))
    d = xs.map(lambda x: x*2).subscribe(print)
    print('-'*20 + '[MERGE]' + '-'*20)
    xs = Observable.range(1, 5)
    ys = Observable.from_('abcde')
    zs = xs.merge(ys).subscribe(print)
    
    # a is before b, and 1 is before 2
    # but you can not guarantee that a is before 1!