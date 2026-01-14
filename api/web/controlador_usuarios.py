from bd import obtener_conexion
from flask import session

# Función para login de usuario
def login_usuario(email, password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT email FROM usuarios WHERE email=%s AND password=%s", (email, password))
            usuario = cursor.fetchone()
            if usuario is None:
                ret = {"status": "ERROR", "mensaje": "Usuario/password erroneo"}
            else:
                session["email"] = usuario['email']
                ret = {"status": "OK"}
        code = 200
        conexion.close()
    except Exception as e:
        print("Excepción al validar usuario:", e, flush=True)
        ret = {"status": "ERROR"}
        code = 500
    return ret, code

# Función para registrar usuario nuevo
def alta_usuario(email, password, name):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT email FROM usuarios WHERE email=%s", (email,))
            existe = cursor.fetchone()
            if existe is None:
                cursor.execute("INSERT INTO usuarios(email,password,name) VALUES (%s,%s,%s)", (email,password,name))
                conexion.commit()
                ret = {"status": "OK"}
                code = 200
            else:
                ret = {"status": "ERROR", "mensaje": "Usuario ya existe"}
                code = 200
        conexion.close()
    except Exception as e:
        print("Excepción al registrar usuario:", e, flush=True)
        ret = {"status": "ERROR"}
        code = 500
    return ret, code

# Función de logout
def logout():
    session.clear()
    return {"status": "OK"}, 200
