from random import randint

class Die:
	"""docstring for Die"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		self.side = randint(1,self.sides)
		print(self.side)

# list = []
# for i in range(10):
# 	die_i = Die()
# 	die_i.roll_die()
# 	list.append(die_i.side)
# 	# print(list)
# 	while i == 9:
# 		print(list)
# 		break

list = []
for i in range(10):
	die_i = Die(sides=10)
	die_i.roll_die()
	list.append(die_i.side)
	# print(list)
	while i == 9:
		print(list)
		break

	



