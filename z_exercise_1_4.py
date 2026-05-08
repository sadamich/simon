### https://runestone.academy/ns/books/published/pythonds/Introduction/Exercises.html


### Implement the remaining relational operators

### (__gt__, __ge__, __lt__, __le__, and __ne__)


print((2).__add__(2))


def gcd(m,n):
    while m%n!=0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def show(self):
        print(self.num,"/",self.den)
    def __add__(self, other):
        newnum = self.num * other.den + \
                 self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    
x = Fraction(1,3)
y = Fraction(1,3)
print(x+y)
print(x>y)
print(x<y)
print(x==y)
