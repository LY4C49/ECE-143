class multinominal:
    def __init__(self,probability):
        self.probability=probability
    
    def generate_sample(self,n):
        import random
        res=[0 for i in range(len(self.probability))]
        candidates=[i for i in range(len(self.probability))]
        for _ in range(n):
            x=random.choices(population=candidates,weights=self.probability,k=1)
            res[x[0]]+=1
        return res
            
def multinomial_sample(n:int,p:list,k=1) -> list:
    """_summary_

    Args:
        n (int): _description_
        p (list): _description_
        k (int, optional): _description_. Defaults to 1.

    Returns:
        list: _description_
    """
    assert isinstance(n,int)
    assert isinstance(p,list)
    assert sum(p)==1
    for v in p:
        assert 0<=v<=1
    assert isinstance(k,int) and k>=1
    multi_sampler=multinominal(probability=p)
    ans=[]
    for _ in range(k):
        sample=multi_sampler.generate_sample(n)
        ans.append(sample)
    return ans

if __name__=="__main__":
    print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
    
    