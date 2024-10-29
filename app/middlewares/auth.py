import jwt
import os
from dotenv import load_dotenv
from functools import wraps
from flask import request, jsonify, current_app

def auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        
        try:
            # Eliminar "Bearer " del token si está presente
            if token.startswith("Bearer "):
                token = token[7:]
            
            # load_dotenv()
            # current_app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Cargar la clave secreta
            # print(current_app.config)


            # Verificar el token y obtener el payload
            payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            request.id = payload['id']  # Guarda el id en el request

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)
    
    return decorated
