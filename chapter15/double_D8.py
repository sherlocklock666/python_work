from random import randint
# import unittest

class Double_D8:

	def __init__ (self, num_sides=8):
		self.num_sides = num_sides

	def roll_num (self):
		number = randint(1,self.num_sides)
		return number

# if __name__ == "__main__":
# 	unittest.main()

# double_D8 = Double_D8()
# double_D8.roll_num()

