# Permite compatibilidad con impresión estilo Python 3
from __future__ import print_function

# request: para leer datos enviados por el cliente
# Blueprint: para agrupar rutas relacionadas
# jsonify: para devolver respuestas en formato JSON
from flask import request, Blueprint, jsonify

# Importamos funciones auxiliares (aunque aquí no se use directamente Encoder)
from funciones_auxiliares import Encoder

# Importamos el controlador donde está la lógica de negocio
import controlador_usuarios


# --------------------------------------------------
# Creamos un Blueprint para las rutas de usuarios
# Todas las rutas tendrán como prefijo /api/usuarios
# --------------------------------------------------
bp = Blueprint('usuarios', __name__, url_prefix="/api/usuarios")


# --------------------------------------------------
# Ruta de LOGIN
# Método: POST
# URL: /api/usuarios/login
# --------------------------------------------------
@bp.route("/login", methods=['POST'])
def login():
    # Obtenemos el tipo de contenido enviado por el cliente
    content_type = request.headers.get('Content-Type')

    # Comprobamos que el contenido sea JSON
    if (content_type == 'application/json'):
        # Leemos el JSON enviado
        login_json = request.json

        # Extraemos usuario y contraseña
        username = login_json['username']
        password = login_json['password']

        # Llamamos a la función de login del controlador
        respuesta, code = controlador_usuarios.login_usuario(username, password)
    else:
        # Si no es JSON, devolvemos error
        respuesta = {"status": "Bad request"}
        code = 401

    # Devolvemos la respuesta al cliente
    return jsonify(respuesta), code


# --------------------------------------------------
# Ruta de REGISTRO de usuarios
# Método: POST
# URL: /api/usuarios/registro
# --------------------------------------------------
@bp.route("/registro", methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        # Leemos los datos enviados en formato JSON
        login_json = request.json

        # Extraemos los datos del usuario
        username = login_json['username']
        password = login_json['password']
        profile = login_json['profile']

        # Llamamos al controlador para dar de alta al usuario
        respuesta, code = controlador_usuarios.alta_usuario(username, password, profile)
    else:
        respuesta = {"status": "Bad request"}
        code = 401

    return jsonify(respuesta), code


# --------------------------------------------------
# Ruta de LOGOUT
# Método: GET
# URL: /api/usuarios/logout
# --------------------------------------------------
@bp.route("/logout", methods=['GET'])
def logout():
    # Llamamos al controlador para cerrar sesión
    respuesta, code = controlador_usuarios.logout()

    # Devolvemos respuesta al cliente
    return jsonify(respuesta), code
