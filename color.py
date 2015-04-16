from enum import Enum

class Color(Enum):
    """
    A class representing the colors in magic the gathering.
    Colorless is not a color. See Rule 203.2c.
    """
    white = "white", "w"
    blue = "blue", "u"
    black = "black", "b"
    red = "red", "r"
    green = "green", "g"


    def __init__(self, long_name: str, abbreviation: str) -> None:
        """
        :param long_name: the full name of the color
        :param abbreviation: color abbreviation
        :return: None
        """
        self.long_name = long_name
        self.abbreviation = abbreviation

    def __str__(self) -> str:
        return str(self.__class__.__name__) + " " + self.long_name
