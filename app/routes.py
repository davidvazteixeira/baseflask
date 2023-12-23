from flask import Flask, render_template
from app.database.models import *
from app import app
import random

@app.route('/')
def index():
    #Users.create(username='Meusa')
    return render_template('index.html')

@app.route('/update')
def update():
    user = User.select(User).where(User.username=='simple_alfa')
    user[0].number = 1
    user[0].save()
    return render_template('index.html')

# Add new routes:
#
#@app.route('/page')
#def page():
#   return render_template('page.html')
