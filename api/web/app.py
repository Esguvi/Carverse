from flask import Flask, jsonify
import os

# Importamos los blueprints de cada módulo
from rutas_usuarios import bp as usuarios_bp
from rutas_coches import bp as coches_bp
from rutas_ficheros import bp as ficheros_bp
from rutas_comentarios import bp as comentarios_bp

def create_app():
    # Creamos la aplicación Flask
    app = Flask(__name__)

    # Clave secreta para sesiones (login/logout)
    app.secret_key = "carshop-secret-key"

    # Activamos debug para desarrollo
    app.config.setdefault('DEBUG', True)

    # Registramos los blueprints con sus URLs
    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
    app.register_blueprint(coches_bp, url_prefix='/api/coches')
    app.register_blueprint(ficheros_bp, url_prefix='/api/ficheros')
    app.register_blueprint(comentarios_bp, url_prefix='/api/comentarios')

    # Manejador global de errores 500
    @app.errorhandler(500)
    def server_error(error):
        print('Excepción durante la petición:', error, flush=True)
        return jsonify({"status": "Internal Server Error"}), 500

    return app

if __name__ == '__main__':
    # Creamos la app
    app = create_app()

    # Leemos host y puerto desde variables de entorno, con valores por defecto
    port = int(os.environ.get('PORT', 8080))
    host = os.environ.get('HOST', '0.0.0.0')

    # Arrancamos el servidor Flask
    app.run(host=host, port=port)
