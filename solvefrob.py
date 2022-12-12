import numpy as np
import itertools as it

def possible_comb(limit,repeat):
    l=[i for i in range(limit+1)]
    return list(it.product(l,repeat=repeat))
    
def solvefrob(coefs,b):
    """_summary_

    Args:
        coefs (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(coefs,list)
    assert isinstance(b,int)
    for co in coefs:
        assert isinstance(co,int)
        assert co>=1
    assert b>0
    
    candidates=possible_comb(b,len(coefs))
    
    candidates=np.array(candidates)
    coefs=np.array(coefs)
    
    all_possible=coefs*candidates
    
    ans=[]
    for i in range(len(all_possible)):
        if np.sum(all_possible[i])==b:
            ans.append(tuple(candidates[i].tolist()))
    
    return ans
    

if __name__=="__main__":
    solvefrob([1,2,3,5],10) 
    
    
    
    