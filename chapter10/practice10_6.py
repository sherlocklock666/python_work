
while 1:
	first_number = input("Please enter first number: ")
	second_number = input("Please enter second number: ")
	
	try:
		anwser = int(first_number) + int(second_number)
	except ValueError :
		print("Sorry, you don't enter a number!")	
	else:
		print(anwser)