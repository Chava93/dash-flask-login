import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import server, app
from flask_login import logout_user, current_user
from views import login, fail, success

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
html.Div(id="page_content")
])


@app.callback(
    Output("page_content", "children"),
    [Input("url", "pathname")])
def display_page(path):
    if path == "/" or path == "/login":
        return login.layout
    elif path == '/fail':
            return login.layout
    elif path == '/success':
        print("success")
        if current_user.is_authenticated:
            return success.layout
        else:
            return login.layout
if __name__ == "__main__":
    app.run_server(debug=True)
