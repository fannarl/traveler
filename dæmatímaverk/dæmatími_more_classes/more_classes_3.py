class Rectangle:
    def __init__(self, __len, __width):
        self.__len = __len
        self.__width = __width

    def __str__(self):
        return 'Length: {}, Width: {}'.format(self.__len, self.__width)

    def __repr__(self):
        return 'Rectangle({},{})'.format(self.__len, self.__width)

    def area(self):
        if self.__len > 0 and self.__width > 0:
            return (self.__len * self.__width)
        else:
            return 0

    def perimeter(self):
        if self.__len >= 0 and self.__width >= 0:
            return 2*(self.__len + self.__width)
        else:
            if self.__len < 0:
                self.__len = 0
            elif self.__width < 0:
                self.__width = 0
            return 2*(self.__len + self.__width)

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False


a = Rectangle()
b = Rectangle(2,3)
print(a)
print(a.area())
print(a.perimeter())
print(a.__repr__())
print(a == b)