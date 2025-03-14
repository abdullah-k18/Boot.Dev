class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        area = self.__length * self.__width
        return area

    def get_perimeter(self):
        perimeter =  2 * (self.__length + self.__width)
        return perimeter


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

