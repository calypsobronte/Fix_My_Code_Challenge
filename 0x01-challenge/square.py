#!/usr/bin/python3
""" I love geometry! """


class Square():
    """ class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Init square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def permiter_of_my_square(self):
        """ perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ exec """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())