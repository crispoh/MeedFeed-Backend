import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound, Unauthorized
from .models import Medico
from . import db 

medicos_blueprint = Blueprint('medicos', __name__)


############### ingresar medico #######################
@medicos_blueprint.route('/registro', methods=['POST'])
def index():
  ####Autorizacion####
  if not check_token():
        raise Unauthorized

  datos = request.get_json()

  medico = Medico(**datos)

  db.session.add(medico)
  db.session.commit()

  return medico_a_dict(medico), 201

################ mostrar lista de medicos ##############
@medicos_blueprint.route('/medicos', methods=['GET'])
def listar_medicos():

    ####Autorizacion####
    if not check_token():
        raise Unauthorized

    medicos = Medico.query.all()

    lista_medicos = []

    for medico in medicos:
      lista_medicos.append(medico_a_dict(medico))

    return jsonify (lista_medicos), 200

################## mostrar por id ######################
@medicos_blueprint.route('/medicos/<id>', methods=['GET'])
def obtener_medico(id):
    ####Autorizacion####
    if not check_token():
        raise Unauthorized

    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()

    #if not medico: 
    #    return NotFound

    return medico_a_dict(medico), 200

################## modificar datos de id ########################
@medicos_blueprint.route('/medicos/<id>', methods=['PUT'])
def actualizar_medico(id):

    ####Autorizacion####
    if not check_token():
        raise Unauthorized

    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()
    datos = request.get_json()

    medico.email = datos['nombre']
    medico.password = datos['password']

    db.session.add(medico)
    db.session.commit()

    return medico_a_dict(medico), 200

################# eliminar datos de id #########################
@medicos_blueprint.route('/medicos/<id>', methods=['DELETE'])
def eliminar_medico(id):

    ####Autorizacion####
    if not check_token():
        raise Unauthorized

    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()

    db.session.delete(medico)
    db.session.commit()

    return '', 204
################ login con jwt ##################################
@medicos_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    datos = request.get_json()
    
    medico  = Medico.query.filter_by(
        email=datos['email'],password=datos['password']).first()

    if medico is None: 
        raise NotFound

    ##Secret Code##
    secret = 'GtP4CVkAxMx2KjKy'

    payload = {
        'sub' : medico.id,
        'iat' : datetime.utcnow(),
        'exp' : datetime.utcnow() + timedelta(days=1)
    }

    return jwt.encode(payload, secret, algorithm='HS256')

################ datos ################################
def medico_a_dict(medico):
  return {
        'id': medico.id,
        'email': medico.email,
        'nombre' : medico.nombre,
        'password' : medico.password
  }
##############def autorizacion##########################

def check_token():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return False

    ### divide el entre BEARER Y EL CODE ###
    partes = auth_header.split(' ')
    ### verifica
    if len(partes) != 2:
        return False

    token = partes[1]
    ##Secret Code##
    secret= 'GtP4CVkAxMx2KjKy'

    try:
      payload = jwt.decode(token, secret, algorithms=['HS256'])

      exp = payload['exp']

      if datetime.utcnow() > datetime.fromtimestamp(exp):
          return False
      
      return True
    except:
      return False