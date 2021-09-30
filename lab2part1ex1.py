"""
1. Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods
that calculate the perimeter and the area of the rectangle. Also, provide setter and getter for the length
and width attributes. The setter should verify that length and width are each floating-point numbers larger
than 0.0 and less than 20.0.
"""


class Rectangle(object):

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def get_width(self):
        return self.width

    def set_width(self, value):
        try:
            self.width = value
            float(value)
            return True
        except ValueError:
            return False

    def get_length(self):
        return self.length

    def set_length(self, value):
        try:
            self.length = value
            float(value)
            return True
        except ValueError:
            return False

    def perimeter(self):
        # calculate the perimeter
        return 2 * (self.width + self.length)

    def area(self):
        # calculate the area
        return self.width * self.length


figure = Rectangle()
figure.set_width(4)
figure.set_length(5)
print("Length of rectangle : ", figure.length)
print("Width of rectangle : ", figure.width)
print("Area of rectangle : ", figure.area())
print("Perimeter of rectangle : ", figure.perimeter())
