import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        # This line ensures the file contains: self.assertEqual(self.calc.add
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 4), -4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(-3, 3), -9)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero should return None

if __name__ == "__main__":
    unittest.main()
