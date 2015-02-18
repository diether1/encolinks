# encoding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

# Flask app
app = Flask("encolinks")
app.config.from_pyfile('settings.py')

# SQLAlchemy
db = SQLAlchemy(app)
from encolinks.models import Link
try:
    db.create_all()
    db.session.commit()
except:
    pass

# Flask Bootstrap
Bootstrap(app)

# Blueprints
from encolinks.rest_api import rest_api
from encolinks.pages import pages

app.register_blueprint(pages)
app.register_blueprint(rest_api, url_prefix='/api')

