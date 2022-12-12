def slide_window(x,width,increment):
    '''
    Implement a sliding window for an arbitrary input list. 
    The function should take the window width and the window increment as inputs 
    and should produce a sequence of overlapping lists from the input list. 
    For example, given x=list(range(15)), the following is the output given a window width of 5 and window increment of 2.
    '''
    assert isinstance(x,list)
    assert isinstance(width,int)
    assert isinstance(increment,int)
    assert width>0
    assert increment>0

    start,end=0,width
    output=[]
    while(end<len(x)):
        output.append(list(x[start:end]))
        start+=increment
        end+=increment
    return output

# if __name__=='__main__':
#     print(slide_window(list(range(18)),5,2))