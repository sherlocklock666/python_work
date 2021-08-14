import json

def greet_user(filename):

	try:
		with open(filename,'r', encoding='utf-8') as f:
			username = json.load(f)
	# except json.decoder.JSONDecodeError:
	# 	print('error')#检测出json文件内容为空
	except FileNotFoundError:
		with open(filename, 'w') as f:
			username = input('What is your name? ')
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}")
	else:
		print(f"Welcome back, {username}!")

message = greet_user("username.json")