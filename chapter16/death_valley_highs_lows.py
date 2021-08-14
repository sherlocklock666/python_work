import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename, 'r') as f:
	reader = csv.reader(f)
	head_row = next(reader)

# for index, head_column in enumerate(head_row):
# 	print(index, head_column)

	dates, highs, lows = [], [], []
	for row in reader:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {date}")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="green")
ax.set_title("2018年每日气温变化\n美国加利福尼亚州死亡谷", fontsize=16)
ax.set_xlabel("日期", fontsize=15)
x_major_locator = plt.MultipleLocator(15)
ax.xaxis.set_major_locator(x_major_locator)
ax.set_ylabel("温度（F）", fontsize=15)

ax.tick_params(
	axis="both", which="major", labelsize=15, 
	direction="inout", length=8, width=5, pad=5,
	labelcolor="grey"
	)
fig.autofmt_xdate()

plt.rcParams['font.sans-serif'] = ['simsun']
plt.show()
