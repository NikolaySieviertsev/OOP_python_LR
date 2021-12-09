"""
2.
TI-01
Create a class CALENDAR. Define methods for creating and working with a CALENDAR instances and overload operations^
"+=, -=" - for adding and subtracting days, months, years to a given date
"==, ! =, >, >=, <, <=" - for comparing dates.
"""

EACH_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Calendar:
    """
    Class CALENDAR contains date elements and defines methods for creating and working with instances
     and overloaded operations.
    """

    def __init__(self, year, month, day):
        """
        Constructor for arguments such as year, month and day.
        """
        if not isinstance(year, int):
            raise TypeError('Error: year has incorrect type!')
        if not isinstance(month, int):
            raise TypeError('Error: month has incorrect type!')
        if not isinstance(day, int):
            raise TypeError('Error: day has incorrect type!')
        if not 0 < year < 2500:
            raise ValueError('Error: year has to be in 1 till 2500 range!')
        if not 1 <= month <= 12:
            raise ValueError('Error: month has to be in 1 till 12 range!')
        if month == 2 and year % 4 == 0 and (year % 400 == 0 and year % 100 != 0):
            days_number = 29
        else:
            days_number = EACH_MONTH[month]
        if not 1 <= day <= days_number:
            raise ValueError('Error: day value is out of range!')
        self._year = year
        self._month = month
        self._day = day

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def date(self):
        return self.year, self._month, self._day  # tuple

    @year.setter
    def year(self, year):
        self._year = year

    @month.setter
    def month(self, month):
        self._month = month

    @day.setter
    def day(self, day):
        self._day = day

    def __iadd__(self, other):
        """
        number_a += number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        _year = self._year + other._year
        _month = self._month + other._month
        _day = self._day + other._day

        if _day > EACH_MONTH[self._month]:
            _day %= EACH_MONTH[self._month]
            _month += 1
        if _month > 12:
            _month %= 12
            _year += 1
        return Calendar(_year, _month, _day)

    def __isub__(self, other):
        """
        number_a -= number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        _year = self._year - other._year
        _month = self._month - other._month
        _day = self._day - other._day
        if _day < 0:
            _month -= 1
            _day = EACH_MONTH[_month] + _day
        if _month < 1:
            _year -= 1
            _month = 12
        return Calendar(_year, _month, _day)

    def __eq__(self, other):
        """
        number_a == number_b
        """

        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date == other.date

    def __ne__(self, other):
        """
        number_a != number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date != other.date

    def __lt__(self, other):
        """
        number_a < number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date < other.date

    def __le__(self, other):
        """
        number_a <= number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date <= other.date

    def __gt__(self, other):
        """number_a > number_b """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date > other.date

    def __ge__(self, other):
        """
        number_a >= number_b
        """
        if not isinstance(other, Calendar):
            raise TypeError('Incorrect type!')
        return self.date >= other.date

    def __str__(self):
        """
        Method to return the date in string form,
         using American date style.
        """
        return f'{self._month}.{self._day}.{self._year}'


date_1 = Calendar(2021, 12, 8)
date_2 = Calendar(2002, 11, 3)
date_3 = Calendar(2002, 11, 3)
date_4 = Calendar(2025, 12, 8)
date_5 = Calendar(1995, 4, 13)
date_6 = Calendar(3, 2, 15)

print("American usage calls for a month/day/year date format :")
print(date_1)
print(date_5)

print(date_1 == date_2)
print(date_3 != date_2)

print(date_4)
date_4 += date_6
print(date_4)
date_4 -= date_6
print(date_4)

print(date_1 > date_2)
print(date_1 != date_2)
print(date_1 <= date_2)
print(date_1 < date_2)
print(date_1 >= date_2)
