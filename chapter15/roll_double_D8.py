from double_D8 import Double_D8
from plotly.graph_objs import Bar, Layout
from plotly import offline

D8_1, D8_2 = Double_D8(), Double_D8()

results = [D8_1.roll_num() + D8_2.roll_num() for roll_num in range(1000)]

max_result = D8_1.num_sides + D8_2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]

x_values = list(range(2, max_result+1))
y_values = frequencies
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title':'掷的点数', 'dtick':1}
y_axis_config = {'title':'出现的次数'}
my_layout = Layout(
	{"title":{'text':'同时掷两个D8的骰子的结果', 'font':{'family':'simsun','size':20}, 'x':0.5}},
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='roll_double_D8.html')
