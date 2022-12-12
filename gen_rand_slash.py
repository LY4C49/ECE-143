import numpy as np
import random
import itertools as it
class SlashMatrix:
    def __init__(self,m,n) -> None:
        assert isinstance(m,int)
        assert isinstance(n,int)
        assert m>1 and n>1

        self.m=m
        self.n=n
        self.initMatrix=np.zeros((m,n))
        self.result=self.initMatrix
    
    def all_combination(self):
        start_x=[i for i in range(self.m-1)]
        start_y=[i for i in range(self.n-1)]
        length=[i for i in range(1,min(self.m,self.n))]
        
        for c in it.product(start_x,start_y,length):
            if self.isValid(c):
                yield c
    
    def isValid(self,c):
        start_x,start_y,length=c
        return True if start_x+length<self.m and start_y+length<self.n else False
    
    
    def get_graph(self,direction):
        assert direction=="back" or direction=="forward"
        self.result=self.initMatrix
        
        choices=self.all_combination()
        
        r,c,l=random.choice(list(choices))
        
        position=[]
        for i in range(l+1):
            position.append((r+i,c+i))
        
        for pos in position:
            self.result[pos[0],pos[1]]=1
        
        if direction=="forward":
            self.result=np.flip(self.result,axis=0)
        
        return self.result

def gen_rand_slash(m=6,n=6,direction="back"):
    """_summary_

    Args:
        m (int, optional): _description_. Defaults to 6.
        n (int, optional): _description_. Defaults to 6.
        direction (str, optional): _description_. Defaults to "back".
    """
    assert isinstance(m,int)
    assert isinstance(n,int)
    assert m>1 and n>1
    
    s=SlashMatrix(m,n)
    return s.get_graph(direction)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(10, 10, sharex=True, sharey=True)
    for ax in axs.flatten():
        image = gen_rand_slash()
        ax.imshow(image, cmap=plt.cm.gray_r)
    plt.show()

    