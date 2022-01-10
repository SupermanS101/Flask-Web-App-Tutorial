from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlite3
from sqlite3 import Error

db = SQLAlchemy()
database = "IDWMUA.sqlite"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    conn = create_connection(database)
    cur = conn.cursor()

    """def load_user(id):
        return User.query.get(int(id))"""

    return app

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        print("Database connection established")
        return conn
    except Error as e:
            print(e)
    return None