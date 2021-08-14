import json

filename = 'number.json'
with open(filename, 'r') as f:
	numbers = json.load(f)
print(numbers)