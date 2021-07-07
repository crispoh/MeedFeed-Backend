from . import db

class Medico (db.Model):
    id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    email = db.Column (db.String, nullable=False)
    password = db.Column (db.String, nullable=False)
    
  #  def __init__(self, email, password):
  #   self.email = email
  #   self.password = password
