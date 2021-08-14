import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.employee = Employee('fang', 'zhiheng', 8000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 13000)

	def test_give_custom_raise(self):
		self.employee.give_raise(8000)
		self.assertEqual(self.employee.salary, 16000)

if __name__ == "__main__":
	unittest.main()