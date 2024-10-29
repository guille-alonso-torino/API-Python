#__init__.py: Inicializa la aplicación, registra los blueprints (rutas), carga variables de entorno y habilita CORS.

from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS

def create_app():

    #cargar variables de entorno
    load_dotenv()
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Cargar la clave secreta

    app.config['host_cd'] = os.getenv('host_cd')
    app.config['port_cd'] = os.getenv('port_cd')
    app.config['database_cd'] = os.getenv('database_cd')
    app.config['password_cd'] = os.getenv('password_cd')
    app.config['user_cd'] = os.getenv('user_cd')

    app.config['host'] = os.getenv('host')
    app.config['port'] = os.getenv('port')
    app.config['database'] = os.getenv('database')
    app.config['password'] = os.getenv('password')
    app.config['user'] = os.getenv('user')
    

    # Habilitar CORS para todas las rutas y orígenes
    CORS(app)

    # Registrar blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/usuarios')

    from app.routes.atencion_ciudadana_routes import atCiudadana_bp
    app.register_blueprint(atCiudadana_bp, url_prefix='/reclamos')

    return app
