from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * (self.__radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.__radius

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


figures = [
    Rectangle(3, 5),
    Circle(8),
    Triangle(3, 4, 5)
]

for figure in figures:
    print(f"{figure.__class__.__name__} - Area: {figure.area()}, Perimeter: {figure.perimeter()}")