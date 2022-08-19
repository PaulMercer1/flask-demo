from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=environ.get("db_connection"),
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY=secrets.token_hex(8)
)

# Create db object
db = SQLAlchemy(app)

from application import routes