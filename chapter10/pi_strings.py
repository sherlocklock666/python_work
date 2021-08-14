# filename = 'pi_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# pi_strings = ''
# for line in lines:
# 	pi_strings += line.strip()

# print(pi_strings)
# print(len(pi_strings))


filepath = '源代码文件/chapter_10/pi_million_digits.txt'

with open(filepath) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
 	print("Yes!")
else:
 	print("Sorry!")
 	
