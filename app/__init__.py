from flask import Flask

app = Flask(__name__)

from app.configs import configs, base
from app.database import adapter
from app.database.models import *
from app import routes
