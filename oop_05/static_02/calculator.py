# attributes { length, width, color, model }
import math


class Calculator:
    def __init__(self, length, width, color, model):
        self.__length = length
        self.__width = width
        self.__color = color
        self.__model = model

    # Accessors [ Getters & Setters ]
    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    # Extra Methods

    # instance method : because it depends on instance attributes : __length, __width
    def calc_body_area(self):
        return self.__length * self.__width

    # static method : because it doesn't depend on instance attributes -
    # result doesn't change from object to another for the same parameters
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
