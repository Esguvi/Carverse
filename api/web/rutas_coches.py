from flask import request, Blueprint, jsonify
import controlador_coches

bp = Blueprint('coches', __name__)

@bp.route("/", methods=["GET"])
def coches():
    respuesta, code = controlador_coches.obtener_coches()
    return jsonify(respuesta), code

@bp.route("/<int:id>", methods=["GET"])
def coche_por_id(id):
    respuesta, code = controlador_coches.obtener_coche_por_id(id)
    return jsonify(respuesta), code

@bp.route("/", methods=["POST"])
def guardar_coche():
    if request.is_json:
        data = request.json
        respuesta, code = controlador_coches.insertar_coche(
            data["nombre"], data["descripcion"], float(data["precio"]), data.get("foto"), data.get("marca")
        )
    else:
        respuesta, code = {"status":"Bad request"}, 401
    return jsonify(respuesta), code

@bp.route("/<int:id>", methods=["DELETE"])
def eliminar_coche(id):
    respuesta, code = controlador_coches.eliminar_coche(id)
    return jsonify(respuesta), code

@bp.route("/", methods=["PUT"])
def actualizar_coche():
    if request.is_json:
        data = request.json
        respuesta, code = controlador_coches.actualizar_coche(
            data["id"], data["nombre"], data["descripcion"], float(data["precio"]),
            data.get("foto"), data.get("marca")
        )
    else:
        respuesta, code = {"status":"Bad request"}, 401
    return jsonify(respuesta), code
