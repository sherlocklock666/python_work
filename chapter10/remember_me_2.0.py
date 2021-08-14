import json

def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename,'r',encoding='utf-8') as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username


def get_new_username():
	username = input('What is your name? ')
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		return username


def verify_username():
	username = get_stored_username()
	message = input(f"If you are {username}, please enter 'Y',"
		"or else enter 'N': 	")
	if message == "Y":
		print(f"Welcome back, {username}!")
	elif message == "N":
		greet_user()
	else:
		print("Please enter by the right format")


def greet_user():
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}")

verify_username()
		
		

	

