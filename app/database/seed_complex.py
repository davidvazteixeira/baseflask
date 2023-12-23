from app.database.models import *

class SeedComplex():
  def __init__(self):
    self.simple_first = True
    self.use_complex = True
    self.use_simple = True

  def populate(self):
    # Seed data
    User.create(username='complex_alpha')
    User.create(username='complex_beta')
    User.create(username='complex_delta')
    User.create(username='complex_gamma')
