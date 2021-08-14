filename = "practice10_1.txt"

with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		line = line.strip()
		print(line.replace('Python','Java'))