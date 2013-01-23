# -*- coding:utf-8 -*-
__author__ = 'aliven.cen'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://webpy:webpy@localhost/webpy'
app.config['SQLALCHEMY_ECHO'] = True
db_sqlite = SQLAlchemy(app)