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
def login_usuario(username, password):
    try:
        # Abrimos conexión con la base de datos
        conexion = obtener_conexion()

        # Creamos un cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # Consulta SQL para comprobar usuario y contraseña
            cursor.execute(
                "SELECT perfil FROM usuarios WHERE usuario = %s AND clave = %s",
                (username, password)
            )

            # Obtenemos el resultado
            usuario = cursor.fetchone()

            # Si no existe el usuario
            if usuario is None:
                ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
            else:
                # Guardamos el usuario en la sesión
                session["usuario"] = username

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
def alta_usuario(username, password, perfil):
    try:
        conexion = obtener_conexion()

        with conexion.cursor() as cursor:
            # Comprobamos si el usuario ya existe
            cursor.execute(
                "SELECT perfil FROM usuarios WHERE usuario = %s",
                (username,)
            )
            usuario = cursor.fetchone()

            # Si el usuario no existe
            if usuario is None:
                # Insertamos el nuevo usuario
                cursor.execute(
                    "INSERT INTO usuarios(usuario,clave,perfil) "
                    "VALUES('" + username + "','" + password + "','" + perfil + "')"
                )

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
