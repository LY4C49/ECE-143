from time import sleep
import random
from datetime import datetime
import itertools as it
import types

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime

def tracker(p,limit=3):
    '''

    The code below defines a generator that returns the duration of its lifetime when called.

    from time import sleep
    import random
    from datetime import datetime
    import itertools as it
    
    def producer():
        'produce timestamps'    
        starttime = datetime.now()
        while True:
            sleep(random.uniform(0,0.2))
            yield datetime.now()-starttime

 
    Note that the output of producer has a seconds attribute. Write a generator that tracks the output of this producer and ultimately returns the number of odd numbered seconds that have been iterated over. The usage pattern is the following,

    >>> t = tracker(p,limit=2)
    >>> next(t)
    1
    >>> list( tracker(p,limit=2))
    [1,2] 
    The limit keyword argument is the number of odd-numbered seconds to track until completion.

    >>> list( tracker(p,limit=5))
    [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5] 
    The last line is interesting because is shows that the producer's seconds value output was an even number for the first six iterations. Your tracker generator should also receive input that changes the existing limit,

    >>> t = tracker(p,limit=3)
    >>> next(t)
    0
    >>> next(t)
    0
    >>> t.send(5)
    1
    >>> list(t)
    [1, 1, 1, 1, 2, 3, 4, 5]

    '''

    assert isinstance(p,types.GeneratorType)
    assert isinstance(limit,int)
    i=0
    while(True):
        sec=next(p).total_seconds()

        if sec%2!=0:
            i+=1
        
        if i>limit:
            break
        
        receive=yield i
        # At beginning, receive is Nones
        if receive is not None:
            assert isinstance(receive,int) and receive>0
            limit=receive


# if __name__ == '__main__':
#     p = producer()
#     t = tracker(p, limit=5)
#     print(next(t))
#     t.send(30)
#     print(list(t))
#     t = tracker(p, limit=3)
#     next(t)
#     t.send('a')


