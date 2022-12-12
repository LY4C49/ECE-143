def next_permutation(t:tuple)->tuple:
    """
    Args:
        t (tuple): _description_

    Returns:
        tuple: _description_
    """
    assert isinstance(t,tuple)
    assert len(t)>0
    
    t_set=set()
    for element in t:
        assert isinstance(element,int)
        assert 0<=element<len(t)
        assert element not in t_set
        t_set.add(element)
        
    t_list=list(t)
    i=len(t_list)-2
    while i>=0 and t_list[i]>t_list[i+1]:
        i-=1
    
    if i!=-1:
        
        j=len(t_list)-1
        while j>i and t_list[j]<t_list[i]:
            j-=1
        
        t_list[i],t_list[j]=t_list[j],t_list[i]
    
    left,right=i+1,len(t_list)-1
    while left<right:
        t_list[left],t_list[right]=t_list[right],t_list[left]
        left+=1
        right-=1
    
    return tuple(t_list)

if __name__=="__main__":
    print(next_permutation((0, 5, 2, 1, 4, 7, 3, 6)))
    
    
    