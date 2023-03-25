from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


import inspect                                                              
import pkgutil                                                                 
import importlib                                                               
import sys 

app = Flask(__name__, template_folder='views')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# db.init_app(app)
from app.models import *

from app import routes
from app import models, views

from .cli import dropdb_command, initdb_command
app.cli.add_command(dropdb_command)
app.cli.add_command(initdb_command)


