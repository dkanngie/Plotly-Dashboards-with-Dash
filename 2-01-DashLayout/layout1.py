# -*- coding: utf-8 -*-

import dash
#from jupyter_dash import JupyterDash # if you want to run it via jupyter

import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
#app = JupyterDash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                {'x': [1, 2, 3], 'y': [8, 2, 1], 'type': 'bar', 'name': 'Berlin'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

#import plotly.offline as pyo
#import plotly.graph_objs as go
#fig = go.Figure(data=figure['data'], layout=figure['layout'])
#pyo.plot(fig)


if __name__ == '__main__':
    app.run_server()

#app.run_server(mode='inline')

