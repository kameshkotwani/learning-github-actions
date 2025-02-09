import unittest

from linting_python import add,mul,substract
class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(1,2), 3)

    def test_subtraction(self):
        self.assertEqual(substract(5,3), 2)

    def test_multiplication(self):
        self.assertEqual(mul(3,4), 12)


if __name__ == '__main__':
    unittest.main()