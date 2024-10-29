from app.config.conexionSQL_atCiudadana import crear_conexion, cerrar_conexion
from flask import jsonify

def obtener_procedimientos():
    # Crear la conexión a la base de datos
    conexion = crear_conexion()
    
    # Verificar si la conexión fue exitosa
    if conexion:
        try:
            # Crear un cursor para ejecutar la consulta
            cursor = conexion.cursor(dictionary=True)
            
            # Ejecutar la consulta para obtener todos los registros de la tabla 'empleado'
            cursor.execute("SELECT routine_name FROM information_schema.routines WHERE routine_type = 'PROCEDURE' AND routine_schema = 'ciudadano'")
            
            # Obtener todos los resultados de la consulta
            results = cursor.fetchall()
            
            # Devolver los resultados en formato JSON
            return jsonify({"results":results})
        
        except Exception as e:
            # Manejar errores de la base de datos
            return jsonify({"mensaje": f"Error al obtener procedimientos: {str(e)}"}), 500
        
        finally:
            # Asegurarse de cerrar la conexión
            cerrar_conexion(conexion)
    
    else:
        # Si no se pudo conectar a la base de datos
        return jsonify({"mensaje": "Error en la conexión a la base de datos"}), 500
    

    
def ejecutar_procedimiento(procedimientoAlmacenado,desde,hasta):
    conexion = crear_conexion()
    # Verificar si la conexión fue exitosa
    if conexion:
        try:
            # Crear un cursor para ejecutar la consulta
            cursor = conexion.cursor(dictionary=True)
            
            # Ejecutar la consulta para obtener todos los registros de la tabla 'empleado'
            cursor.callproc(procedimientoAlmacenado, [desde, hasta])
            
            # Obtener todos los resultados de la consulta
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()

            # Devolver los resultados en formato JSON
            return jsonify({"resultado":[results]})
        
        except Exception as e:
            # Manejar errores de la base de datos
            return jsonify({"mensaje": f"Error al ejecutar procedimientos: {str(e)}"}), 500
        
        finally:
            # Asegurarse de cerrar la conexión
            cerrar_conexion(conexion)
    
    else:
        # Si no se pudo conectar a la base de datos
        return jsonify({"mensaje": "Error en la conexión a la base de datos"}), 500