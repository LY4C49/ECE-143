# fill out the necessary methods shown below and add others if need be.
"""_summary_

Returns:
    _type_: _description_
"""

class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    def __repr__(self):
        return "Interval("+str(self._a)+","+str(self._b)+")"
        
    def __eq__(self,other):
        return True if self._a==other._a and self._b==other._b else False
    
    def __lt__(self,other):
        return True if self._b <= other._a else False
    
    def __gt__(self,other):
        return True if self._a >= other._b else False
    
    def __ge__(self,other):
        return True if self._a > other._a and self._a < other._b <= self._b else False
    
    def __le__(self,other):
        return True if self._a <= other._a and other._a < self._b <= other._b else False
    
    def __add__(self,other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        if self < other:
            return [self, other]
        elif self <= other:
            return self.__class__(self._a, other._b)
        elif self._a>=other._a and self._b<=other.b:
            return other
        elif self == other:
            return self
        elif self._a<=other._a and self._b>=other._b:
            return self
        elif self >= other:
            return self.__class__(other._a, self._b)
        elif self > other:
            return [other, self]

if __name__=="__main__":
    r=Interval(1,3)+Interval(2,4)
    print(r)