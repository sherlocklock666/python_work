filename = "practice10_1.txt"

with open(filename) as file_object:
	# contents = file_object.read()
	# for i in range(1,4):
	# 	print(contents+"\n")
	
	# for line in file_object:
	# 	print(line.rstrip())
	
	contents = file_object.readlines()
	for content in contents:
		print(content.strip())

