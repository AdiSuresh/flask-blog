from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# TODO: just testing
app = Flask(__name__)
app.config['SECRET_KEY'] = '5aa3ea1e9b440a835563af017f35faef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
