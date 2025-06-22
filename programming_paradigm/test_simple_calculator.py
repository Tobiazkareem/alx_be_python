#Writing unit testing for a simple calculator class
#Import the necessary modules
import unittest
from simple_calculator import SimpleCalculator

#Define a Test Class
class TestSimpleCalculator(unittest.Testcase):

#create test methods for each operations
	def setUp(self):
		"""Set up the SimpleCalculator instance before each test."""
		self.calc = SimpleCalculator()

	def test_addition(self):
		"""Test the addition method."""
		self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(-1, 1), 0)
		#Add more assertions to thoroughly test the add method.

	def test_subtraction(self):
		"""Test the substraction method."""
		self.assertEqual(self.calc.substract(3, 2), 1)
		self.assertEqual(self.calc.substract(5, 6), -1)

	def test_multiplication(self):
		"""Test the multiplication method."""
		self.assertEqual(self.calc.multiply(2, 3), 6)
		self.assertEqual(self.calc.multiply(8, 2), 16)

	def test_division(self):
		"""Test various division..."""
		self.assertEqual(self.calc.divide(10, 2), 5)
		self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")

	def test_division_edge_cases(self):
		"""Test edge cases for division."""
		self.assertEqual(self.calc.divide(0, 5), 0)
		self.assertIsNone(self.calc.divide(0, 0), "0 divided by 0 should return None")

if __name__ == '__main__':
	unittest.main()	
