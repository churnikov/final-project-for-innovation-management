import pandas as pd
import json
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
plotly.offline.init_notebook_mode(connected=True)

with open('dangers.json', 'r') as f:
    jsn = json.load(f)

index = []
columns = ['Вероятность наступления', 'Сила влияния', 'Мероприятие', 'Статегия']
values = []

def get_prob_idx(prob):
    if prob < 0.1:
        return 0
    elif 0.1 <= prob <= 0.4:
        return 1
    elif 0.41 <= prob <= 0.70:
        return 2
    elif 0.71 <= prob <= 0.99:
        return 3


def split_text(text, line_size=10):
    if len(text.split()) > line_size:
        text = ' '.join(t if i % line_size != 0 else t+'<br>'
        for i, t in enumerate(text.split()))
    return text


for k, r in jsn.items():
    index.append(k)
    values.append((get_prob_idx(r[columns[0]]), r[columns[1]],
                                r[columns[2]], r[columns[3]]))
df = pd.DataFrame(data=values, index=index, columns=columns)

data = [
    go.Scatter(
        x=[x1],
        y=[x2],
        mode='markers',
        name=f'{x1, x2}',
        text=[split_text(t) + split_text(f'<br>Мероприятие: {x3}')
              + split_text(f'<br>Статегия: {x4}')]
    )
    for x1, x2, x3, x4, t in zip(df[columns[1]].values, df[columns[0]].values,
                                 df[columns[2]].values, df[columns[3]].values,
                                 index)
]

layout = go.Layout(
    title='Риски',
    xaxis={
        "title": columns[1]
        },
    yaxis={
        "title": columns[0]
        }
)

iplot({'data': data, 'layout': layout})
