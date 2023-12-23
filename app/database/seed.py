from app.database.models import *
import yaml

class Seed():
  def __init__(self):
    import app.database.seed_complex
    
    #with open('simple_seed.yml') as f:
    #  app.db_conf = yaml.safe_load(f)

    # Seed data
    #Users.create(username='alpha')
    #Users.create(username='beta')
    #Users.create(username='delta')
    #Users.create(username='gamma')
