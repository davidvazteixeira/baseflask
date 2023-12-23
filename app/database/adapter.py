# PeeWee docs:
# http://docs.peewee-orm.com/en/latest/index.html

from app import app
from app import hooks
import yaml
import peewee as pw
import os

# Databse configurarion file
with open('database.yml') as f:
  app.db_conf = yaml.safe_load(f)

dbtype = app.db_conf['adapter']['type']

if dbtype == 'none':
  app.db = None

elif dbtype == 'sqlite':
  database_name = app.db_conf['adapter']['database_name']
  path = "sqlite_database"
  if not os.path.exists(path):
    os.makedirs(path) 
  
  app.db = pw.SqliteDatabase(f"{path}/{database_name}")

elif dbtype == 'postgresql':
  database_name = app.db_conf['adapter']['database_name']
  user = app.db_conf['adapter']['user']
  password = app.db_conf['adapter']['password']
  host = app.db_conf['adapter']['host']
  port = app.db_conf['adapter']['port']
  app.db = pw.PostgresqlDatabase(database_name, user=user, password=password, host=host, port=port)

elif dbtype == 'mysql':
  database_name = app.db_conf['adapter']['database_name']
  user = app.db_conf['adapter']['user']
  password = app.db_conf['adapter']['password']
  host = app.db_conf['adapter']['host']
  port = app.db_conf['adapter']['port']
  charset = app.db_conf['adapter']['charset']
  app.db = pw.MySQLDatabase(database_name, user=user, password=password, host=host, port=port, charset=charset)

else:
  print("Problem in database.yml")
  print(f"type: <{dbtype}> is not recognized")
  print("use: none, sqlite, postgresql or mysql")
  exit()
