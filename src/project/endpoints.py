from flask import Blueprint, request, jsonify
from .models import Medico
from . import db 

medicos_blueprint = Blueprint('medicos', __name__)


############### ingresar medico #######################
@medicos_blueprint.route('/registro', methods=['POST'])
def index():
  datos = request.get_json()

  medico = Medico(**datos)

  db.session.add(medico)
  db.session.commit()

  return medico_a_dict(medico), 201

################ mostrar lista de medicos ##############
@medicos_blueprint.route('/medicos', methods=['GET'])
def listar_medicos():

    medicos = Medico.query.all()

    lista_medicos = []

    for medico in medicos:
      lista_medicos.append(medico_a_dict(medico))

    return jsonify (lista_medicos), 200

################## mostrar por id ######################
@medicos_blueprint.route('/medicos/<id>', methods=['GET'])
def obtener_medico(id):
    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()

    #if not medico: 
    #    return NotFound

    return medico_a_dict(medico), 200

################## modificar id ########################
@medicos_blueprint.route('/medicos/<id>', methods=['PUT'])
def actualizar_medico(id):
    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()
    datos = request.get_json()

    medico.email = datos['nombre']
    medico.password = datos['password']

    db.session.add(medico)
    db.session.commit()

    return medico_a_dict(medico), 200

################# eliminar id #########################
@medicos_blueprint.route('/medicos/<id>', methods=['DELETE'])
def eliminar_medico(id):
    medico = Medico.query.get_or_404(id)
    #medico = Medico.query.filter_by(id=id).first()

    db.session.delete(medico)
    db.session.commit()

    return '', 204

################ datos ################################
def medico_a_dict(medico):
  return {
        'id': medico.id,
        'email': medico.email
  }
