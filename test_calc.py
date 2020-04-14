import unittest

class Calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalc(unittest.TestCase):
    def test_add(self):
        sum = Calc()
        self.assertEqual(sum.add(10, 5), 10)
