import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline

url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

data = [{
	'type': 'bar',
	'x': repo_names,
	'y': stars,
	'hovertext': labels,
	'marker': {
	'color': 'rgb(205, 133, 0)',
	'line': {'width': 1.5, 'color': 'rgb(139, 87, 66)'}
	},
	'opacity': 0.5
}]

my_layout = {
	'title': "Github上最受欢迎的Python项目",
	'titlefont': {'size':28, 'family':"simsun"},
	'xaxis': {
	'title': 'Repository',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}
	},
	'yaxis': {
	'title': 'Stars',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}
	}
}

# data = [Bar(x=repo_names, y=stars)]
# x_axis_config = {'title': '仓库名称', 'dtick':1}
# y_axis_config = {'title': '收藏数量'}
# my_layout = Layout(
# 	title={
# 	'text':"Github上最受欢迎的Python项目",
# 	'font':{'family':'fangsong', 'size':20},
# 	'x':0.5
# 	},
# 	xaxis=x_axis_config, yaxis=y_axis_config)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
