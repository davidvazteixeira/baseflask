from app import app
from app.database.base_model import BareModel, SimpleModel
from peewee import *
import datetime
import random

class User(SimpleModel):
    username = CharField(unique = True)



