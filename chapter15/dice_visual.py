from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(5000):
	result = die_1.roll() +die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (1, max_result+1):
	frequence = results.count(value)
	frequencies.append(frequence)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'结果', 'dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(
	{"title": {"text": "'掷一个D6和一个D10骰子5000次的结果'", "font": {"family": "STKaiti", "size": 30}, "x": 0.5}},
	# title='掷两个D6骰子5000次的结果',
	xaxis=x_axis_config, yaxis=y_axis_config,
	)

offline.plot({'data':data, 'layout':my_layout}, filename='D10_D6.html')

