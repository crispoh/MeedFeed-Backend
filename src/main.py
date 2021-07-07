#from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from werkzeug.exceptions import NotFound
from project import create_app

app = create_app()