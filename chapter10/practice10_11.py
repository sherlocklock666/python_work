import json

filename = 'favorite_number.json'
try:
	with open(filename, 'r') as f:
		message2 = json.load(f)	
except FileNotFoundError:
	with open(filename, 'w') as f:
		message1 = input("Please enter your favorite number: ")
		json.dump(message1, f)
		print(f"Your favorite number is {message1}")
else:
	print(f"I know your favorite number! it's {message2}")

	