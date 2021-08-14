filename = "源代码文件/chapter_10/alice.txt"

try:
	with open(filename,encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	words = contents.split()
	num_words = len(words)
	print(f"This book {filename} has {num_words} words.")