import plotly.express as px
import json
import pandas as pd


filename = 'all_month.geojson'
with open(filename, 'r', encoding='utf-8') as f:
	all_month_data = json.load(f)

# readable_file = 'readable_all_month_data.json'
# with open(readable_file, 'w') as f:
# 	json.dump(all_month_data, f, indent=4)

all_data_dicts = all_month_data['features']
mags, places, lons, lats = [], [], [], []
for data_dict in all_data_dicts:
	mags.append(data_dict['properties']['mag'])
	places.append(data_dict['properties']['place'])
	lons.append(data_dict['geometry']['coordinates'][0])
	lats.append(data_dict['geometry']['coordinates'][1])

data = pd.DataFrame(
	data=zip(lons, lats, mags, places), 
	columns=('经度', '纬度', '震级', '地点'))
data["震级"] = data["震级"].astype(str)
data.head()

fig = px.scatter(data,
	x='经度', y='纬度',  hover_name='地点',
	color='震级',height=550, width=1100,
	marginal_x='histogram', marginal_y='rug'
	)

fig.update_layout(title={'text':'USGS过去一个月的地震分布散点图',
	'font':{'family':'fangsong', 'size':20},
	'x':0.5, 'y':0.95})

fig.write_html('px画图练习.html')
# fig.show()
