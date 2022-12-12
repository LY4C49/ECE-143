def is_string_integer(x):
    '''
    Takes a single string character (i.e., 'a','b','c') as input and 
    Returns True or False if that character represents a valid integer in base 10.
    :param:x:int
    :return:bool

    '''
    assert isinstance(x,str)
    if ord("9")>=ord(x)>=ord("0"):
        return True
    else:
        return False
