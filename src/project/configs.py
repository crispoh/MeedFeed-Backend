class Config: 
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@db:5432/medfeedbase'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  #Mostrar consultas en consola
  SQLALCHEMY_ECHO = True
  #LOG = False
