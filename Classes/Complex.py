import math

class Complex(object):
    def __init__(self, real, imaginary):
          self.real = real
          self.imag = imaginary
    def __add__(self, no):
        return Complex(self.real + no.real,
                       self.imag + no.imag)
    def __sub__(self, no):
        return Complex(self.real - no.real,
                       self.imag - no.imag)
    def __mul__(self, no):
        return Complex(self.real*no.real - self.imag*no.imag,
                       self.imag*no.real + self.real*no.imag)
    def __truediv__(self, no):
             sr, si, otherr, otheri = self.real, self.imag, no.real, no.imag # short
             r = float(otherr**2 + otheri**2)
             return Complex((sr*otherr+si*otheri)/r, (si*otherr-sr*otheri)/r)
    def mod(self):
         return Complex(pow(self.real**2+self.imag**2, 0.5), 0)
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')