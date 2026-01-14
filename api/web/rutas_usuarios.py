from flask import request, Blueprint, jsonify
import controlador_usuarios

bp = Blueprint('usuarios', __name__)

@bp.route("/login", methods=['POST'])
def login():
    if request.is_json:
        data = request.json
        respuesta, code = controlador_usuarios.login_usuario(data['email'], data['password'])
    else:
        respuesta, code = {"status":"Bad request"}, 401
    return jsonify(respuesta), code

@bp.route("/registro", methods=['POST'])
def registro():
    if request.is_json:
        data = request.json
        respuesta, code = controlador_usuarios.alta_usuario(data['email'], data['password'], data['name'])
    else:
        respuesta, code = {"status":"Bad request"}, 401
    return jsonify(respuesta), code

@bp.route("/logout", methods=['GET'])
def logout():
    respuesta, code = controlador_usuarios.logout()
    return jsonify(respuesta), code
