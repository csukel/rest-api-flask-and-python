import unittest

var1 , var2 = 5, 5
num1, num2 = 2, 8

class TestVariables(unittest.TestCase):

	def test_equal(self):
		self.assertEqual(var1, var2)

	def test_mutliply(self):
		self.assertEqual(num1 * num2, 16, "Test 2")

if __name__ == '__main__':
    unittest.main()