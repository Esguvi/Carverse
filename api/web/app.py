# Importamos Flask para crear la aplicación web
# jsonify se usa para devolver respuestas en formato JSON
from flask import Flask, jsonify

# os permite leer variables de entorno (HOST, PORT, etc.)
import os

# Función para cargar variables de entorno (opcional en Docker)
from variables import cargarvariables


# Función que crea y configura la aplicación Flask
def create_app():
    # Creamos la aplicación Flask
    app = Flask(__name__)

    # --------------------------------------------------
    # Clave secreta de la aplicación
    # Es necesaria para manejar sesiones (login/logout)
    # --------------------------------------------------
    app.secret_key = "carshop-secret-key"

    # --------------------------------------------------
    # Configuración de la aplicación
    # DEBUG=True permite ver errores detallados
    # --------------------------------------------------
    app.config.setdefault('DEBUG', True)

    # --------------------------------------------------
    # Registro de Blueprints
    # Cada blueprint representa un conjunto de rutas
    # Se usan para organizar el proyecto por módulos
    # --------------------------------------------------

    # Rutas relacionadas con usuarios (login, registro, logout)
    from rutas_usuarios import bp as usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')

    # Rutas relacionadas con coches
    from api.web.rutas_coches import bp as coches_bp
    app.register_blueprint(coches_bp, url_prefix='/api/coches')

    # Rutas relacionadas con ficheros
    from rutas_ficheros import bp as ficheros_bp
    app.register_blueprint(ficheros_bp, url_prefix='/api/ficheros')

    # Rutas relacionadas con comentarios
    from rutas_comentarios import bp as comentarios_bp
    app.register_blueprint(comentarios_bp, url_prefix='/api/comentarios')

    # --------------------------------------------------
    # Manejador global de errores 500 (error interno)
    # Se ejecuta si ocurre una excepción no controlada
    # --------------------------------------------------
    @app.errorhandler(500)
    def server_error(error):
        # Se imprime el error en consola (útil para depuración)
        print('An exception occurred during a request. ERROR:' + error, flush=True)

        # Respuesta JSON estándar para el cliente
        ret = {"status": "Internal Server Error"}
        return jsonify(ret), 500

    # Devolvemos la aplicación ya configurada
    return app


# --------------------------------------------------
# Punto de entrada de la aplicación
# Solo se ejecuta si el archivo se lanza directamente
# --------------------------------------------------
if __name__ == '__main__':
    # Creamos la app
    app = create_app()

    # Cargar variables de entorno si no se usan contenedores
    # cargarvariables()  # ocultar en caso de lanzar todos los contenedores

    try:
        # Leemos el puerto y el host desde variables de entorno
        port = int(os.environ.get('PORT'))
        host = os.environ.get('HOST')

        # Arrancamos el servidor Flask
        app.run(host=host, port=port)
    except:
        # Mensaje si ocurre un error al arrancar el servidor
        print("Error starting server", flush=True)
