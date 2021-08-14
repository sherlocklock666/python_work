from matplotlib import pyplot as plt
import matplotlib

font ={'family':'MicroSoft YaHei'} #win可以显示中文
matplotlib.rc("font",**font)

x=range(2,26,2)
y=[15,13,14.5,34,23,6,26,26,27,22,18,17]

#这里是与折线图的唯一区别  -->散点图
plt.scatter(x,y,label='3月份')
#设置刻度
_xtick_labels=["3月{}日".format(i) for i in x]

plt.xticks(list(x)[::2],_xtick_labels[::2]) #加个步长，使刻度稀疏

#添加图例
plt.legend()

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("记录3月份温度变化")
plt.show()
