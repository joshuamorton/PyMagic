import unittest
from color import Color

class TestColor(unittest.TestCase):

    def test_color_comparison(self):
        self.assertTrue(Color.white < Color.blue < Color.black < Color.red < Color.green)

    def test_le(self):
        self.assertTrue(Color.white <= Color.white)

    def test_ge(self):
        self.assertTrue(Color.green >= Color.green >= Color.red >= Color.black)

    def test_gt(self):
        self.assertTrue(Color.green > Color.red > Color.black > Color.blue > Color.white)

    def test_str(self):
        self.assertEqual("Color red", str(Color.red))
        