# # import matplotlib
# # matplotlib.rc("font", family="MicroSoft YaHei")
# import matplotlib

# font ={'family':'MicroSoft YaHei'} #win可以显示中文
# matplotlib.rc("font",**font)
import matplotlib.pyplot as plt 
# plt.style.use("seaborn")
fig, ax = plt.subplots()
x_vaules = range(1, 1001)
y_vaules = [x**2 for x in x_vaules]
ax.scatter(x_vaules, y_vaules , s=10, c=y_vaules, cmap=plt.cm.Reds)
ax.axis([0, 1100, 0, 1100000])

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='y', which='major', labelsize=14, colors='green')
ax.tick_params(pad=10, direction='inout', length=4, width=2)

plt.rcParams['font.sans-serif']=['simsun']
plt.savefig('squares_plot.png', bbox_inches='tight')