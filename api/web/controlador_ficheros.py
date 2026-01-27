import os


def guardar_fichero(nombre, contenido):
    try:
        print(nombre, flush=True)
        basepath = os.path.dirname(__file__)  # ruta del archivo actual
        ruta_fichero = os.path.join(basepath, '..', 'apache', 'static', 'archivos', nombre)
        
        os.makedirs(os.path.dirname(ruta_fichero), exist_ok=True)
        
        print('Archivo guardado en ' + ruta_fichero, flush=True)
        contenido.save(ruta_fichero)
        
        respuesta = {"status": "OK"}
        code = 200
    except Exception as e:
        print("Excepción al guardar el fichero:", e, flush=True)
        respuesta = {"status": "ERROR", "mensaje": str(e)}  # Agregar detalles del error
        code = 500
    return respuesta, code


def ver_fichero(nombre):
    try:
        basepath = os.path.dirname(__file__)  # ruta del archivo actual
        ruta_fichero = os.path.join(basepath, '..', 'apache', 'static', 'archivos', nombre)
        
        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            salida = f.read()
        
        respuesta = {"contenido": salida}
        code = 200
    except Exception as e:
        print("Excepción al ver el fichero:", e, flush=True)
        respuesta = {"contenido": "", "mensaje": str(e)}  # Agregar detalles del error
        code = 500
    return respuesta, code
