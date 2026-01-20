import os
import pymysql

def obtener_conexion():
    # Conexión a MariaDB usando variables de entorno
    return pymysql.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'),
        port=int(os.environ.get('DB_PORT', 3306)),
        db=os.environ.get('DB_DATABASE'),
        cursorclass=pymysql.cursors.DictCursor  # Devuelve resultados como diccionario
    )

