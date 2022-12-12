"""_summary_

Returns:
    _type_: _description_
"""
from math import sqrt
class Rational:
    """_summary_
    """

    def __init__(self, n, d) -> None:
        """_summary_

        Args:
            n (_type_): _description_
            d (_type_): _description_
        """
        assert isinstance(n, int) and isinstance(d, int)
        self.numerator = n
        self.denominator = d
        # print(self.numerator,self.denominator)
        self.GCD = self._findGCD()
        self.numerator /= self.GCD
        self.denominator /= self.GCD
        self.numerator = int(self.numerator)
        self.denominator = int(self.denominator)
        # print(self.numerator,self.denominator,self.GCD)

    def _findGCD(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        x, y = abs(self.numerator), abs(self.denominator)
        while(x != y):
            if x > y:
                x -= y
            else:
                y -= x
        # n=d return whaterve n or d
        return x

    def findGCD(x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        x, y = abs(x), abs(y)
        while(x != y):
            if x > y:
                x -= y
            else:
                y -= x
        # n=d return whaterve n or d
        return x

    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator)+'/'+str(self.denominator)

    def __int__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return int(self.numerator/self.denominator)

    def __float__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return float(float(self.numerator)/float(self.denominator))

    def __add__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            n = self.numerator+other*(self.denominator)
            res = Rational(n=n, d=self.denominator)
            return res
        else:
            d = self.denominator*other.denominator
            n = (self.numerator*other.denominator) + \
                (other.numerator*self.denominator)
            return Rational(n=n, d=d)

    def __radd__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            n = self.numerator+other*(self.denominator)
            res = Rational(n=n, d=self.denominator)
            return res
        else:
            d = self.denominator*other.denominator
            n = (self.numerator*other.denominator) + \
                (other.numerator*self.denominator)
            return Rational(n=n, d=d)

    def __sub__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            n = self.numerator-other*(self.denominator)
            res = Rational(n=n, d=self.denominator)
            return res
        else:
            d = self.denominator*other.denominator
            n = (self.numerator*other.denominator) - \
                (other.numerator*self.denominator)
            return Rational(n=n, d=d)

    def __rsub__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            n = self.numerator-other*(self.denominator)
            res = Rational(n=n, d=self.denominator)
            return res
        else:
            d = self.denominator*other.denominator
            n = (self.numerator*other.denominator) - \
                (other.numerator*self.denominator)
            return Rational(n=n, d=d)

    def __truediv__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            return Rational(n=self.numerator, d=self.denominator*other)
        else:
            return Rational(n=(self.numerator*other.denominator), d=(self.denominator*other.numerator))

    def __rtruediv__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            # print("here")
            n = other*self.denominator
            # print(n,self.numerator)
            return Rational(n=n, d=self.numerator)
        else:
            n = self.numerator*other.denominator
            d = self.denominator*other.numerator
            return Rational(n=n, d=d)

    def __neg__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return Rational(n=-self.numerator, d=self.denominator)

    def __mul__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            return Rational(n=self.numerator*other, d=self.denominator)
        else:
            return Rational(n=self.numerator*other.numerator, d=self.denominator*other.denominator)

    def __rmul__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            return Rational(n=self.numerator*other, d=self.denominator)
        else:
            return Rational(n=self.numerator*other.numerator, d=self.denominator*other.denominator)

    def __lt__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            return True if float(self.numerator/self.denominator) < other else False
        else:
            return True if (self.numerator*other.denominator) < (other.numerator*self.denominator) else False
    
    def __gt__(self,other):
        """_summary_

        Args:
            other (_type_): _description_
        """
        assert isinstance(other,int) or isinstance(other,Rational)
        if type(other)==int:
            return True if float(self.numerator/self.denominator) > other else False
        else:
            return True if (self.numerator*other.denominator) > (other.numerator*self.denominator) else False

    def __eq__(self, other):
        """_summary_

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        assert isinstance(other, int) or isinstance(other, Rational)
        if type(other) == int:
            return True if self.numerator == other and self.denominator == 1 else False
        else:
            return True if self.numerator == other.numerator and self.denominator == other.denominator else False


def square_root_rational(x: Rational, abs_tol: Rational = Rational(1, 1000)) -> Rational:

    """_summary_

    Args:
        x (Rational): _description_
        abs_tol (Rational, optional): _description_. Defaults to Rational(1,1000).

    Returns:
        Rational: _description_
    """
    assert x>0
    assert abs_tol>0
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)

    left, right = 0, x

    while(True):
        mid = (left+right)/2
        square = mid*mid

        if(abs(float(mid)-sqrt(float(x))) < float(abs_tol)):
            return mid

        else:
            if square < x:
                left = mid
            else:
                right = mid


# if __name__ == "__main__":

#     r = Rational(3, 4)
#     print(repr(r))

#     p = Rational(100, 10)
#     print(repr(p))

#     print(type(float(r)))
#     # print(int(r),float(r))

#     print(-1/r)

#     print(-Rational(12345, 128191))

#     print(-Rational(12345, 128191) + Rational(101, 103) * 30/44)

#     print(Rational(10, 3) * Rational(101, 8) - Rational(11, 8))

#     print(sorted([Rational(10, 3), Rational(9, 8),
#           Rational(10, 1), Rational(1, 100)]))

#     print(Rational(10, 3) == Rational(3, 4), Rational(
#         10, 3) == Rational(10, 3), Rational(100, 10) == 10)

#     print(Rational(101, 103) * 30)

#     print("abcde", square_root_rational(
#         Rational(1112, 3), abs_tol=Rational(1, 1000)))
