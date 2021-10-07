"""
2. Create a class called Rational for performing arithmetic with fractions. Write a program to test your class.
 Use integer variables to represent the private data of the class – the numerator and the denominator.
 Provide a __init__() method that enables an object of this class to be initialized when it’s declared.
 The __init__() should contain default parameter values in case no initializers are provided and should store
 the fraction in reduced form. For example, the fraction 2/4 would be stored in the object as 1 in the numerator
 and 2 in the denominator. Provide public methods that perform each of the following tasks:
- printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
- printing Rational numbers in floating-point format.
"""

from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Value have to be integer type!")
        if not denominator:
            raise ZeroDivisionError("Division by Zero!")
        temp = gcd(numerator, denominator)
        self.__denominator = denominator // temp
        self.__numerator = numerator // temp

    def rat(self):
        return f'{self.__numerator} / {self.__denominator}'

    def fl(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):

        self_denominator = self.__denominator

        other_denominator = other.__denominator

        return Rational(self.__numerator * other_denominator + other.__numerator * self_denominator,
                        self.__denominator * other_denominator)

    def __sub__(self, other):

        self_denominator = self.__denominator

        other_denominator = other.__denominator

        return Rational(self.__numerator * other_denominator - other.__numerator * self_denominator,
                        self.__denominator * other_denominator)

    def __mul__(self, other):

        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other):

        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)


try:
    number1 = Rational(5, 10)
    number2 = Rational(4, 5)
    number3 = number1 + number2
    print(number1.rat())
    print(number1.fl())
    print(number2.rat())
    print(number2.fl())
    print(number3.rat())
    print(number3.fl())
except AttributeError:
    print("Wrong arguments!")
