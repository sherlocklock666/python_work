import plotly.express as px
import json
import pandas as pd
# import plotly.graph_objects as go

filename = 'eq_data_30_day_m1.json'
with open(filename, 'r') as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, titles, lons, lats, locations= [], [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	title = eq_dict['properties']['title']
	location = eq_dict['properties']['place']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	titles.append(title)
	lons.append(lon)
	lats.append(lat)
	locations.append(location)

data = pd.DataFrame(
	data=zip(lons, lats, titles, mags, locations), 
	columns=['经度', '纬度', '位置', '震级', '坐标']
	)
data.head()

fig = px.scatter(
	data,
	x='经度', y='纬度',
	labels={'x':'经度', 'y':'纬度'},
	range_x=[-200, 200], range_y=[-90,90],
	width=800, height=800,
	size='震级', size_max=10, color='震级',
	hover_name='位置'
	)

fig.update_layout(
	title={
	'text':'全球地震散点图', 'x':0.5
	})
# fig.write_html('global_earthquakes.html')
fig.show()

