import mysql.connector
from mysql.connector import Error
from flask import current_app

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
           host= current_app.config['host_cd'],
           port=current_app.config['port_cd'],
           user=current_app.config['user_cd'],
           database=current_app.config['database_cd'],
           password=current_app.config['password_cd']
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")
