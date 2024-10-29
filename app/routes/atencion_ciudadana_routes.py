from flask import Blueprint, request
from app.controllers.atencion_ciudadana import obtener_procedimientos, ejecutar_procedimiento
from app.middlewares.auth import auth

atCiudadana_bp = Blueprint('atencion_ciudadana', __name__)

@atCiudadana_bp.route('/listarProcedimientos', methods=['GET'])
@auth
def obtener_todos_los_usuarios():
    return obtener_procedimientos()


@atCiudadana_bp.route('/listar', methods=['POST'])
@auth
def ejecutar_procedimiento_almacenado():
     datos = request.get_json()
     procedimientoAlmacenado = datos.get('procedimiento')
     desde = datos.get('desde')
     hasta = datos.get('hasta')
     return ejecutar_procedimiento(procedimientoAlmacenado,desde,hasta)