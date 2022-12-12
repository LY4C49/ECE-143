def get_power_of3(target):
    '''
    Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40. In other words, 
    using the set above and the addition and subtraction operations, 
    construct any integer between 1 and 40 without re-using elements
    '''
    assert isinstance(target,int)
    assert 1<=target<=40

    candidates=[-1,0,1]
    decomposition={}
    nums=[1,3,9,27]
    res=[]
    def backtracking(nums,candidates):
        if len(res)==len(nums):
            comp=0
            for i in range(len(res)):
                comp+=(nums[i]*res[i])
            if 1<=comp<=40:
                decomposition[comp]=list(res)
            return
        
        for i in range(len(candidates)):
            res.append(candidates[i])
            backtracking(nums,candidates)
            res.pop(-1)

    backtracking(nums,candidates)
    return decomposition[target]