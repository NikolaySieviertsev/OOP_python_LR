"""
1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods
that calculate the perimeter and the area of the rectangle. Also, provide setter and getter for the length
and width attributes. The setter should verify that length and width are each floating-point numbers larger
than 0.0 and less than 20.0.
"""


class Rectangle(object):

    def __init__(self, length=1, width=1):
        if not isinstance(length, (int, float)) and isinstance(width, (int, float)):
            raise TypeError("Values have to be integer or float")
        if not (length > 0 and width > 0):
            raise ValueError("Values have to be > 0")
        self._length = length
        self._width = width

    def __str__(self):
        return f"Rectangle({self._length}, {self._width})"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not (isinstance(value, float) and 0.0 < value < 20.0):
            raise Exception("Error! Wrong type and value of width!")
        self._width = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not (isinstance(value, float) and 0.0 < value < 20.0):
            raise Exception("Error! Wrong type and value of length!")
        self._length = value

    def perimeter(self):
        # calculate the perimeter
        return 2 * (self._width + self._length)

    def area(self):
        # calculate the area
        return self._width * self._length


figure = Rectangle()
figure.width = 4.0
figure.length = 5.0
# print(figure.__str__())
print("Length of rectangle : ", figure.length)
print("Width of rectangle : ", figure.width)
print("Area of rectangle : ", figure.area())
print("Perimeter of rectangle : ", figure.perimeter())
