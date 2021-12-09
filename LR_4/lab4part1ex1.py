"""
1. Modify the class Rational of Lab No2 to perform the following tasks:
- adding two Rational numbers. The result should be stored in reduced form;
- subtracting two Rational numbers. The result should be stored in reduced form;
- multiplying two Rational numbers. The result should be stored in reduced form;
- dividing two Rational numbers. The result should be stored in reduced form;
- comparison two Rational numbers.
"""


from math import gcd


class Rational:
    """
    Class Rational is created for performing arithmetic with fractions.
    """

    def __init__(self, numerator=1, denominator=1):
        """
        Constructor for creating numerator and denominator of fractions.
        """
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError('Incorrect type of numerator or denominator!')
        if denominator == 0:
            raise ZeroDivisionError
        greatest_common_divisor = gcd(numerator, denominator)
        self._numerator = numerator // greatest_common_divisor
        self._denominator = denominator // greatest_common_divisor

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, num):
        self._numerator = num

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, num):
        self._denominator = num

    def __add__(self, other):
        """
        fraction_a + fraction_b
        """
        return Rational(self._numerator * other.denominator + self._denominator * self._numerator,
                        self._denominator * other.denominator)

    def __iadd__(self, other):
        """
        fraction_a += fraction_b
        """
        return Rational(self._numerator * other.denominator + self._denominator * self._numerator,
                        self._denominator * other.denominator)

    def __sub__(self, other):
        """
        fraction_a - fraction_b
        """
        return Rational(self._numerator * other.denominator - self._denominator * other.numerator,
                        self._denominator * other.denominator)

    def __isub__(self, other):
        """
        fraction_a -= fraction_b
        """
        return Rational(self._numerator * other.denominator - self._denominator * other.numerator,
                        self._denominator * other.denominator)

    def __mul__(self, other):
        """
        fraction_a * fraction_b
        """
        return Rational(self._numerator * other.numerator, self._denominator * other.denominator)

    def __imul__(self, other):
        """
        fraction_a *= fraction_b
        """
        return Rational(self._numerator * other.numerator, self._denominator * other.denominator)

    def __truediv__(self, other):
        """
        fraction_a / fraction_b
        """
        return Rational(self._numerator * other.denominator, other.numerator * self._denominator)

    def __itruediv__(self, other):
        """
        fraction_a /= fraction_b
        """
        return Rational(self._numerator * other.denominator, other.numerator * self._denominator)

    def __eq__(self, other):
        """
        fraction_a == fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator == other.numerator / other.denominator

    def __le__(self, other):
        """
        fraction_a <= fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator <= other.numerator / other.denominator

    def __lt__(self, other):
        """
        fraction_a < fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator < other.numerator / other.denominator

    def __ge__(self, other):
        """
        fraction_a >= fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator >= other.numerator / other.denominator

    def __gt__(self, other):
        """
        fraction_a > fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator > other.numerator / other.denominator

    def __ne__(self, other):
        """
        fraction_a != fraction_b
        """
        if not isinstance(other, Rational):
            raise TypeError('Incorrect type!')
        return self._numerator / self._denominator != other.numerator / other.denominator

    def __str__(self):
        """
        Method to return the fraction in string form.
        """
        return f'{self._numerator}/{self._denominator}'

    def float_format(self):
        """
        Method to return the fraction in floating-point format.
        """
        return round(self._numerator / self._denominator, 3)


fract_1 = Rational(2, 4)
fract_2 = Rational(5, 6)
fract_3 = Rational(3, 7)
fract_4 = Rational()
fract_5 = Rational(5, 10)
fract_6 = Rational(9, 21)

print(fract_1)
print(fract_2)
print(fract_3)
print(fract_4)
print(fract_1 + fract_2)
print(fract_1 - fract_2)
print(fract_1 * fract_2)
print(fract_1 / fract_2)
print(fract_3.float_format())
print(fract_2.float_format())
print(fract_1 < fract_2)
print(fract_1 > fract_2)
print(fract_1 == fract_2)
print(fract_2 == fract_3)
print(fract_1 != fract_2)
print(fract_1 >= fract_5)
print(fract_3 <= fract_6)
