import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import utils
colors = ["#8c2e2d", "#56565a"]

layout = html.Div([
    html.H1("Has entrado a la página.",className="title")
], className="container")
