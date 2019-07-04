import dash
import pandas as pd
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = dash.Dash(__name__)
app.title = "Login"
server = app.server
app.config.suppress_callback_exceptions = True

## Flask Web Development p.53
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"] ,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy()
db.init_app(server)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    password = db.Column(db.String(128))
    date = db.Column(db.String(20))

    def __repr__(self):
        return f"User {self.name}"


login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
