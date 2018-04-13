"""
The flask application package.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import configparser
import os

def get_db_uri(app, auth):
    dba = auth["database"]
    uri = app["app"]["database"].replace("{user}", dba["user"]).\
        replace("{password}", dba["password"]).\
        replace("{host}", dba["host"]).\
        replace("{db}", dba["name"])
    return uri


cwd = os.getcwd()
config = configparser.ConfigParser()
config.read(cwd + "/tfl_arrivals/app.cfg")

config_auth = configparser.ConfigParser()
config_auth.read(cwd + "/tfl_arrivals/auth.cfg")

app = Flask(__name__)
db_uri = get_db_uri(config, config_auth)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

db = SQLAlchemy(app)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(threadName)s	- %(module)s - %(levelname)s - %(message)s")

fh = logging.FileHandler("arrivals.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

import tfl_arrivals.views
