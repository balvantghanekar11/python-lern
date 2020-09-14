#tut68 abstrac base class

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides="4"

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rec1= Rectangle()
print(rec1.printarea())