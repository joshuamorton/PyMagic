from enum import Enum

class OrderedEnum(Enum):
    """
    an enumeration class that has a well ordering
    """
    def __init__(self, value: int):
        self.value = value

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented


class Color(OrderedEnum):
    white = 0, "white", "w"
    blue = 1, "blue", "u"
    black = 2, "black", "b"
    red = 3, "red", "r"
    green = 4, "green", "g"


    def __init__(self, value: int, long_name: str, abbreviation: str):
        """
        :param value: a value used for ordering/comparison of the colors
        :param long_name: the full name of the color
        :param abbreviation: color abbreviation
        :return:
        """
        self.long_name = long_name
        self.abbreviation = abbreviation

    def __str__(self):
        return str(self.__class__.__name__) + " " + self.long_name
