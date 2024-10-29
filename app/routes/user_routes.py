from flask import Blueprint, request, Flask
from app.controllers.user_controller import obtener_usuarios, agregar_usuario, authUser
from app.middlewares.auth import auth


user_bp = Blueprint('usuarios', __name__)

@user_bp.route('/empleados', methods=['GET'])
def obtener_todos_los_usuarios():
    return obtener_usuarios()

@user_bp.route('/authStatus', methods=['GET'])
@auth
def autenticar_usuario():
    return authUser(request.id)

@user_bp.route('/', methods=['POST'])
def agregar_un_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    return agregar_usuario(nombre)
