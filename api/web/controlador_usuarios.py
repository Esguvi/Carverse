# Función para obtener la conexión con la base de datos
from bd import obtener_conexion

# sys y datetime se importan por si se necesitan en el futuro
import sys
import datetime as dt

# session permite manejar sesiones de usuario en Flask
from flask import session


# --------------------------------------------------
# Función para validar el login de un usuario
# --------------------------------------------------
def login_usuario(email, password):
    try:
        # Abrimos conexión con la base de datos
        conexion = obtener_conexion()

        # Creamos un cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # Consulta SQL para comprobar usuario y contraseña
            cursor.execute("SELECT email FROM usuarios WHERE email = %s AND password = %s",(email, password))
            
            # Obtenemos el resultado
            user = cursor.fetchone()
            
            # Si no existe el usuario
            if user is None:
                ret = {"status": "ERROR","mensaje":"Usuario/password erroneo" }
            else:
                # Guardamos el usuario en la sesión
                session["email"] = user

                # Login correcto
                ret = {"status": "OK"}

        code = 200
        conexion.close()

    except:
        # En caso de error se muestra en consola
        print("Excepcion al validar al usuario", flush=True)
        ret = {"status": "ERROR"}
        code = 500

    return ret, code


# --------------------------------------------------
# Función para registrar un nuevo usuario
# --------------------------------------------------
def alta_usuario(email, password, name):
    try:
        conexion = obtener_conexion()

        with conexion.cursor() as cursor:
            # Comprobamos si el usuario ya existe
            cursor.execute("SELECT name FROM usuarios WHERE email = %s",(email,))
            user = cursor.fetchone()
      
            # Si el usuario no existe
            if user is None:
                # Insertamos el nuevo usuario
                cursor.execute("INSERT INTO usuarios (email, password, name) VALUES (%s, %s, %s)",(email, password, name))
                
                # Comprobamos si se insertó correctamente
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret = {"status": "OK"}
                    code = 200
                else:
                    ret = {"status": "ERROR"}
                    code = 500
            else:
                # Usuario ya existente
                ret = {"status": "ERROR", "mensaje": "Usuario ya existe"}
                code = 200

        conexion.close()

    except:
        print("Excepcion al registrar al usuario", flush=True)
        ret = {"status": "ERROR"}
        code = 500

    return ret, code


# --------------------------------------------------
# Función de LOGOUT
# Elimina los datos de sesión del usuario
# --------------------------------------------------
def logout():
    # Borra toda la información almacenada en la sesión
    session.clear()

    # Devuelve confirmación
    return {"status": "OK"}, 200
