import csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from datetime import datetime 

filename = "sitka_weather_07-2018 simple.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
# 	for index, column_header in enumerate(header_row):
# 		print(index, column_header)
	lows, highs, dates = [], [], []
	for row in reader:
		high = int(row[6])
		low = int(row[7])
		date = datetime.strptime(row[2], '%Y-%m-%d')
		highs.append(high)
		dates.append(date)
		lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="green", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

x_major_locator = MultipleLocator(30)
y_major_locator = MultipleLocator(5)

ax.set_title ("2018年全年每日气温", fontsize=20)
ax.set_xlabel ("2018年各月份", fontsize=16)
ax.set_ylabel ("温度(F)", fontsize=16)
ax.tick_params(axis='both', which="major", labelsize=20)
fig.autofmt_xdate()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.rcParams["font.sans-serif"] = ['simsun']

plt.show()


