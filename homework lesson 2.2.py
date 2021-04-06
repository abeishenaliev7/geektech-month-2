class Complex:
    def __int__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        (self.a + other.a) + (self.b + other.b)

    def __mul__(self, other):
        (self.a * other.a - self.b * other.b) + (self.b * other.a + self.a * other.b)

    def __truediv__(self, other):
        return

    def __sub__(self, other):
        return



complex1 = complex(5, 7)
complex2 = complex(6, 9)
add = complex1.__add__(complex2)
print(add)
print()
mul = complex1.__mul__(complex2)
print(mul)
print()
div = complex1.__truediv__(complex2)
print(div)
print()
sub = complex1.__sub__(complex2)
print(sub)





