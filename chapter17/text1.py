import requests
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
import plotly.graph_objects as go

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

fig = go.Figure([go.Bar(y=stars, x=repo_names, hovertext=labels)])


fig.update_traces(marker_color='rgb(205, 133, 0)', 
	marker_line_color='rgb(139, 87, 66)',
	marker_line_width=1.5, opacity=0.6)

fig.update_layout(
    title={
    'text': "Github上最受欢迎的Python项目",
    'y':0.9, 'x':0.5,
    },
    xaxis=dict(
    title='Python项目',
    titlefont_size=16,
    tickfont_size=14,
    ),
    yaxis=dict(
    title='收藏次数',
    titlefont_size=16,
    tickfont_size=14,
    ))
fig.write_html('test.html')
fig.show()