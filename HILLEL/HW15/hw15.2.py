from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        common = gcd(a, b)
        self.a = a // common
        self.b = b // common

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Приклад використання
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a  # 2/3 + 1/2 = 7/6
f_d = f_b * f_a  # 1/2 * 2/3 = 1/3
f_e = f_a - f_b  # 2/3 - 1/2 = 1/6

print(f"f_a: {f_a}")  # Fraction: 2, 3
print(f"f_b: {f_b}")  # Fraction: 1, 2
print(f"f_c = f_a + f_b: {f_c}")  # Fraction: 7, 6
print(f"f_d = f_a * f_b: {f_d}")  # Fraction: 1, 3
print(f"f_e = f_a - f_b: {f_e}")  # Fraction: 1, 6

print(f"f_d < f_c? {f_d < f_c}")  # True
print(f"f_d > f_e? {f_d > f_e}")  # True
print(f"f_a != f_b? {f_a != f_b}")  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
print(f"f_1 == f_2? {f_1 == f_2}")  # True
