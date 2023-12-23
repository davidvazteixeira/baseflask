from flask import Flask, render_template
from app import app

@app.before_request
def _db_connect():
  if app.db:
    app.db.connect()

@app.teardown_request
def _db_close(exc):
  if app.db:
    if not app.db.is_closed():
      app.db.close()
