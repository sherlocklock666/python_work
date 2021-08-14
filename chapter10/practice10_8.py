filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

with open(filename_1,'r') as f_1:
	contents = f_1.read()
	print(contents)

try:
	with open(filename_2,'r') as f_2:
		contents = f_2.read()	
except FileNotFoundError:
	# print("No such file")
	pass
else:
	print(contents)
