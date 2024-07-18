#!/usr/bin/python3
""" A square class """


class Square:
    """ This class defines a square """

    def __init__(self, width=0):
        """ Initialize the square with a given width """
        self.width = width
        self.height = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ This function measures the perimeter of the square """
        return self.width * 4

    def __str__(self):
        """ Public attribute """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
