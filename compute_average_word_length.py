from dis import Instruction


def compute_average_word_length(instring,unique=False):
    '''
    Write a compute_average_word_length(instring,unique=False) function to compute the average length of the words in the input string (instring). 
    If the unique option is True, then exclude duplicated words. 
    Note that the words are case sensitive.
    '''
    assert isinstance(instring,str)
    assert isinstance(unique,bool)

    words=instring.split(" ")
    if unique==True:
        words=set(words)
    
    word_num=len(words)
    word_total_length=0

    for word in words:
        word_total_length+=len(word)
    
    return word_total_length/word_num