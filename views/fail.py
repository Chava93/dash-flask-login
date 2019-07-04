import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import utils
colors = ["#8c2e2d", "#56565a"]

layout = html.Div([
    html.Div([
        html.Div(className = "modal-background"),
        html.Div([
                html.Div([
                    html.Div([
                        html.P("Incorrect user or password, please try again")
                    ],className="notification is-danger"),
                    html.H1('Analysic Nabla', className = 'title', style = {'color':colors[0]}),
                    html.H2('Sign in', className = 'subtitle'),
                    html.P([
                        dcc.Input(className="input is-medium", type="email", placeholder="Email"),
                        html.Span([
                            html.I(className="fas fa-envelope")
                        ],className="icon is-small is-left")
                    ], className="control has-icons-left"),
                    html.Br(),
                    html.P([
                        dcc.Input(className="input is-medium", type="password", placeholder="Password"),
                        html.Span([
                            html.I(className="fas fa-lock")
                        ],className="icon is-small is-left")
                    ], className="control has-icons-left"),
                    html.Br()
                ], className = "box")
            ], className = 'modal-content')
    ], className = 'modal is-active')
], className = 'container')
