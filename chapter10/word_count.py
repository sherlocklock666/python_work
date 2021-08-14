def count_words(filename):

	try:
		with open(filename,encoding='-utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		# print(f"Sorry, the file {filename} does not exist.")
		pass
	else:
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words")

s = '源代码文件/chapter_10/'
filenames = [f'{s}alice.txt',f'{s}diddhartha.txt']
for filename in filenames:
	count_words(filename)