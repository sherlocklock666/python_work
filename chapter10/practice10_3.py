
filename = "guest.txt"

with open(filename,'a') as file_object:
	message = input("请输入你的名字：")
	file_object.write(message)
