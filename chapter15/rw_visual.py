import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	rw = RandomWalk(50_000)
	rw.fill_walk()
	plt.style.use("seaborn")
	fig, ax = plt.subplots(figsize=(15, 9), dpi=125)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_vaules, rw.y_vaules, edgecolors='none',
		c=point_numbers, cmap=plt.cm.Blues, s=1)
	ax.scatter(0, 0, c='red', edgecolors='none', s=50)
	ax.scatter(rw.x_vaules[-1], rw.y_vaules[-1], 
		c='green', edgecolors='none', s=50)
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	message = input("Press any key to continue, or press 'N' to quit: ")
	if message == 'N':
		break




