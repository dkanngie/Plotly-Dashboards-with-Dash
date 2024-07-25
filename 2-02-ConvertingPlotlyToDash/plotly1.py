import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = {
        'size': 12,
        'color': 'rgb(151,4,153)',
        'symbol': 'pentagon',
        'line': {'width': 2}
        }
    )]

layout = go.Layout(
    title = 'Random Data Scatterplot123',
    xaxis = {'title': 'Some random x-values'},
    yaxis = {'title': 'Some random y-values'},
    hovermode='closest'
    )

fig = go.Figure(data=data, layout=layout)

app.layout = html.Div([
    dcc.Graph(id='scatter3a',figure=fig),
    dcc.Graph(id='scatter3b',figure=fig)
])

#app.layout = html.Div([
#    dcc.Graph(
#        id='scatter3',
#        figure=fig, #figure={'data': data, 'layout': layout}
#    )
#])

if __name__ == '__main__':
    app.run_server()
