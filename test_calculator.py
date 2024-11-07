import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_sub(self):
        self.assertEqual(self.calc.subtract(-2,1), -3)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(4,2), 2)
    
    def test_multi(self):
        self.assertEqual(self.calc.multiply(5,7), 35)
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(-5,3), -15)

    def test_divi(self):
        self.assertEqual(self.calc.divide(4,2), 2)
    def test_divi2(self):
        self.assertEqual(self.calc.divide(3,1), 3)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(4,2),0)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(3,2), 1)
if __name__ == '__main__':
    unittest.main()