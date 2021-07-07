from . import db

            ####### Modelo Base de datos ########
### al agregar dato se debe: docker-compose exec flask_app flask db init 
### docker-compose exec flask_app flask db migrate
### docker-compose exec flask_app flask db upgrade

class Medico (db.Model):
    id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column (db.String, nullable=False)
    email = db.Column (db.String, nullable=False)
    password = db.Column (db.String, nullable=False)

             ### ignorar###

  #  def __init__(self, email, password):
  #   self.email = email
  #   self.password = password
