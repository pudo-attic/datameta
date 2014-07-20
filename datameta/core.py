import logging

from flask import Flask
from flask.ext.assets import Environment

from datameta import default_settings
from datameta.catalogs import load_catalogs
from datameta.queue import make_celery

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.from_object(default_settings)
app.config.from_envvar('DATAMETA_SETTINGS', silent=True)

assets = Environment(app)
catalogs = load_catalogs(app)
celery = make_celery(app)
