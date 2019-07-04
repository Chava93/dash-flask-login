import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
from flask_login import login_user
from werkzeug.security import check_password_hash
import utils
from app import server, app, User
import user_manage as UM

DATABASE_URL = os.environ["DATABASE_URL"]
colors = ["#8c2e2d", "#56565a"]

layout = html.Div([
    html.Div([
        dcc.Location(id='url_login', refresh=True),
        html.Div(className = "modal-background"),
        html.Div([
                html.Div([
                    html.H1('Analysic Nabla', className = 'title', style = {'color':colors[0]}),
                    html.H2('Sign in', className = 'subtitle'),
                    html.P([
                        dcc.Input(className="input is-medium", type="email", placeholder="Email", id='email'),
                        html.Span([
                            html.I(className="fas fa-envelope")
                        ],className="icon is-small is-left")
                    ], className="control has-icons-left"),
                    html.Br(),
                    html.P([
                        dcc.Input(className="input is-medium", type="password", placeholder="Password", id='password'),
                        html.Span([
                            html.I(className="fas fa-lock")
                        ],className="icon is-small is-left")
                    ], className="control has-icons-left"),
                    html.Br(),
                    html.Div([
                        html.Div([
                            html.A("Log in",className = 'button is-medium is-primary is-centered', id='login')
                        ], className = 'column is-2 is-offset-5')
                    ], className = 'columns')
                ], className = "box")
            ], className = 'modal-content')
    ], className = 'modal is-active')
], className = 'container')


@app.callback(Output('url', 'pathname'),
              [Input('login', 'n_clicks')],
              [State('email', 'value'),
               State('password', 'value')])
def sucess(n_clicks, email, pwd):
    if n_clicks > 0:
        print(str(User.query.filter_by(email = email).first()))
        user = User.query.filter_by(email = email).first()
        if user:
            if UM.ValidateUsers(DATABASE_URL, email, pwd).validate():
                login_user(user)
                return '/success'
            else:
                return '/fail'
