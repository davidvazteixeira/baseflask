from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

# Add new routes:
#
#@app.route('/page')
#def page():
#   return render_template('page.html')
