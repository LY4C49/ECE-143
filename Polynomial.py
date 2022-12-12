import copy
class Polynomial:
    """
    Create a Python class that can implement a univariate polynomial 
    over the field of integers (only!) with the following operations and interfaces.
    """

    def __init__(self, x: dict) -> None:
        self.exp_coe = x
        self.high = 0
        self.kv = []

        for k, v in x.items():
            assert k>=0 and isinstance(v,int)
            self.high = max(self.high, k)
            self.kv.append((k, v))

        self.kv.sort()
        # print(self.kv)

    def __repr__(self) -> str:
        p = []
        if self.kv == []:
            return "0"
        for k, v in self.kv:
            if k == 0:
                p.append(str(v))
            elif k == 1:
                p.append(str(v)+" x")
            else:
                p.append("{coeff} x^({exp})".format(coeff=str(v), exp=str(k)))
        return " + ".join(p)

    def __mul__(self, other):
        x = {}
        if type(other) == int:
            for k, v in self.kv:
                x[k] = v*other
        elif type(other) == Polynomial:
            kv1 = self.kv
            kv2 = other.kv
            for k1, v1 in kv1:
                for k2, v2 in kv2:
                    if k1+k2 not in x:
                        x[k1+k2] = v1*v2
                    else:
                        x[k1+k2] += (v1*v2)
            print(kv1, kv2, x)
        else:
            raise NotImplementedError(
                "Do not support {type} now".format(type=type(other)))
        return Polynomial(x)

    def __rmul__(self, other):
        if type(other) == int:
            return self.__mul__(other)  # Remeber this example! Helpful!!!
        else:
            raise NotImplementedError(
                "Do not support {type} now".format(type=type(other)))

    def __add__(self, other):
        x = copy.deepcopy(self.exp_coe)
        if type(other) == int:
            if 0 in x:
                x[0] += other
            else:
                x[0] = other

        elif type(other) == Polynomial:
            for k, v in other.kv:
                if k not in x:
                    x[k] = v
                else:
                    x[k] += v
        else:
            raise NotImplementedError(
                "Do not support {type} now".format(type=type(other)))
        return Polynomial(x)

    def __radd__(self, other):
        return self.__add__(other=other)

    def __sub__(self, other):
        x = copy.deepcopy(self.exp_coe)
        if type(other) == int:
            if 0 in x:
                x[0] -= other
            else:
                x[0] = -other

            if x[0] == 0:
                x.pop(0)

        elif type(other) == Polynomial:
            for k, v in other.kv:
                if k not in x:
                    x[k] = -v
                else:
                    x[k] -= v

                if x[k] == 0:
                    x.pop(k)
        else:
            raise NotImplementedError(
                "Do not support {type} now".format(type=type(other)))
        return Polynomial(x)

    def __rsub__(self, other):
        x = copy.deepcopy(self.exp_coe)
        if type(other) == int:
            if 0 in x:
                x[0] = other-x[0]
            else:
                x[0] = other

            if x[0] == 0:
                x.pop(0)

        else:
            raise NotImplementedError(
                "Do not support now")
        return Polynomial(x)

    def __eq__(self, other):
        if type(other) == int:
            if len(self.kv) > 1:
                return False
            elif len(self.kv) == 0:
                return True if other == 0 else False
            else:
                return True if self.exp_coe[0] == other else False
        elif type(other) == Polynomial:
            return True if self.exp_coe == other.exp_coe else False

    def __truediv__(self, other):
        if self.high < other.high:
            raise NotImplementedError(
                "Do not support now")
        if type(other)==Polynomial:
            kvs=[]
            res=self._helper(dividend=self,divisor=other,quotient=kvs)
            #print("hhh",res,kvs)
            if not res:
                raise NotImplementedError(
                "Do not support now")
            else:
                x=dict((k, v) for k, v in kvs)
                return Polynomial(x)
        elif type(other)==int:
            x={}
            for k,v in self.kv:
                x[k]=v/other
                return Polynomial(x)
            
            
    def __rtruediv__(self,other):
        raise NotImplementedError(
                "Do not support now")
        
    def _helper(self, dividend, divisor, quotient):
        if dividend.high == 0:
            #print(dividend.high, dividend)
            return True if dividend == 0 else False
        k = dividend.high-divisor.high
        v = dividend.exp_coe[dividend.high]/divisor.exp_coe[divisor.high]
        if v!=int(v):
            return False
        else:
            v=int(v)
        quotient.append((k, v))
        dividend = dividend-Polynomial({k: v})*divisor
        result = self._helper(dividend, divisor, quotient)
        return True if result else False
    
    def subs(self, x):
        res=0
        for k,v in self.kv:
            res+=(v*(x)**k)
        return res
        


if __name__ == "__main__":
    p = Polynomial({0: 8, 1: 2, 3: 4})
    q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})
    p1 = Polynomial({0: 8})
    p2 = 8
    print(p*q)
    print(3*p)
    print(p-100)
    print(100-p)
    print(p-q)
    print(p-p)
    print(type(p-p))
    print((p-p) == 0)
    print((p-p) == 1)
    print(p1 == p2)
    print(p == q)
    print(p.subs(10))
    print(p*4 + 5 - 3*p - 1)
    p = Polynomial({2:1,0:-1})
    q = Polynomial({1:1,0:-1})
    print("p/q",p/q)
    #print(p  / Polynomial({1:1,0:-3}))
    
