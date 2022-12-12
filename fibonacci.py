def fibonacci(n):
    '''
    The Fibonacci numbers are defined by the following recursion: F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1. 
    Write a generator to compute the first n Fibonacci numbers. 
    For example, for n=10, the output for list(fibonacci(n)) should be [1,1,2,3,5,8,13,21,34,55].
    '''
    assert isinstance(n,int)
    assert n>0

    first,second=1,1
    yield first
    yield second

    for i in range(2,n):
        first,second=second,first+second
        yield second

# if __name__ == '__main__':
#     print(list(fibonacci(10)))
