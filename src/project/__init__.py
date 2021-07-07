from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from weakref.datastructures import auth_property
from .configs import Config
#from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
#bcrypt = Bcrypt()

def register_blueprint(app):
    from .endpoints import medicos_blueprint
    app.register_blueprint(medicos_blueprint)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)

    db.init_app(app)
    migrate.init_app(app, db)
    #bcrypt.init_app(app)
    #ma.init_app(app)

    return app