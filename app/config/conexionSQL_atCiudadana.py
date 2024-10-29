import mysql.connector
from mysql.connector import Error
from flask import current_app

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
           host= current_app.config['host'],
           port=current_app.config['port'],
           user=current_app.config['user'],
           database=current_app.config['database'],
           password=current_app.config['password']
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