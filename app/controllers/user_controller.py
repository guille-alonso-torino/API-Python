from app.config.conexionSQL import crear_conexion, cerrar_conexion
from flask import jsonify

def obtener_usuarios():
    # Crear la conexión a la base de datos
    conexion = crear_conexion()
    
    # Verificar si la conexión fue exitosa
    if conexion:
        try:
            # Crear un cursor para ejecutar la consulta
            cursor = conexion.cursor(dictionary=True)
            
            # Ejecutar la consulta para obtener todos los registros de la tabla 'empleado'
            cursor.execute("SELECT * FROM empleado")
            
            # Obtener todos los resultados de la consulta
            empleados = cursor.fetchall()
            
            # Devolver los resultados en formato JSON
            return jsonify(empleados)
        
        except Exception as e:
            # Manejar errores de la base de datos
            return jsonify({"mensaje": f"Error al obtener empleados: {str(e)}"}), 500
        
        finally:
            # Asegurarse de cerrar la conexión
            cerrar_conexion(conexion)
    
    else:
        # Si no se pudo conectar a la base de datos
        return jsonify({"mensaje": "Error en la conexión a la base de datos"}), 500
    

def authUser(id):
    # Crear la conexión a la base de datos
    conexion = crear_conexion()
    
    # Verificar si la conexión fue exitosa
    if conexion:
        try:
            # Crear un cursor para ejecutar la consulta, diccionario en true para acceder como objeto
            cursor = conexion.cursor(dictionary=True)
            
            # Ejecutar la consulta para obtener todos los registros de la tabla 'persona'
            cursor.execute("SELECT * FROM persona WHERE id_persona = %s", [id])  # Usa %s como marcador de posición

            user = cursor.fetchall()
      
            if(len(user) == 0): 
               return jsonify({"mensaje": "Autenticación fallida"}), 401
            
            # Devolver los resultados en formato JSON, filtrando el campo clave
            for u in user:
                if "clave" in u:
                    del u["clave"]


            return jsonify(user)
        
        except Exception as e:
            # Manejar errores de la base de datos
            return jsonify({"mensaje": f"Error al obtener usuario: {str(e)}"}), 500
        
        finally:
            # Asegurarse de cerrar la conexión
            cerrar_conexion(conexion)
    
    else:
        # Si no se pudo conectar a la base de datos
        return jsonify({"mensaje": "Error en la conexión a la base de datos"}), 500


def agregar_usuario(nombre):
    # Simular que un usuario fue agregado a la base de datos
    return jsonify({"mensaje": f"Usuario {nombre} agregado correctamente"}), 201
