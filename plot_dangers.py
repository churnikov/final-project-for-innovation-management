import pandas as pd
import json
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
plotly.offline.init_notebook_mode(connected=True)

with open('dangers.json', 'r') as f:
    jsn = json.load(f)

index = []
columns = ['Вероятность наступления', 'Сила влияния']
values = []

for k, r in jsn.items():
    index.append(k)
    values.append((r[columns[0]], r[columns[1]]))
df = pd.DataFrame(data=values, index=index, columns=columns)

data = [
    go.Scatter(
        x=[x1],
        y=[x2],
        mode='markers',
        text=[t]
    )
    for x1, x2, t in zip(df[columns[1]].values, df[columns[0]].values, index)
]

layout = go.Layout(
    title='Риски'
)

iplot({'data': data, 'layout': layout})
