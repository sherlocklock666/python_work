import matplotlib
matplotlib.rc("font", family="youyuan")
# font ={'family':'fangsong'} #win可以显示中文
# matplotlib.rc("font",**font)
import matplotlib.pyplot as plt 

plt.style.use("Solarize_Light2")
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()