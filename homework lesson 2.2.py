class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        new_complex = Complex(a, b)
        return new_complex

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.b * other.a + self.a * other.b
        newcoplex = Complex(a, b)
        return newcoplex

    def __truediv__(self, other):
        a = (self.a + self.b) * (other.a - other.b)
        b = (other.a + other.b)
        newcoPlex = Complex(a, b)
        return newcoPlex

    def __str__(self):
        return f"{self.a} + {self.b}i"


c1 = Complex(1, 2)
c2 = Complex(1, 4)

print(c1 + c2)
print(c1 * c2)
print(c1 / c2)
