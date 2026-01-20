from bd import obtener_conexion

def convertir_coche_a_json(coche):
    return {
        "id": coche["id"],
        "nombre": coche["nombre"],
        "descripcion": coche["descripcion"],
        "precio": float(coche["precio"]),
        "foto": coche.get("foto"),
        "marca": coche.get("marca")
    }

def insertar_coche(nombre, descripcion, precio, foto, marca):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO coches(nombre, descripcion, precio, foto, marca) VALUES (%s,%s,%s,%s,%s)",
                (nombre, descripcion, precio, foto, marca)
            )
        conexion.commit()
        conexion.close()
        return {"status":"OK"}, 200
    except:
        return {"status":"ERROR"}, 500

def obtener_coches():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM coches")
            coches = cursor.fetchall()
        conexion.close()
        return [convertir_coche_a_json(c) for c in coches], 200
    except:
        return [], 500

def obtener_coche_por_id(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM coches WHERE id=%s", (id,))
            coche = cursor.fetchone()
        conexion.close()
        return convertir_coche_a_json(coche) if coche else {}, 200
    except:
        return {}, 500

def eliminar_coche(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            ret = {"status": "OK"} if cursor.rowcount else {"status": "Failure"}
        conexion.commit()
        conexion.close()
        return ret, 200
    except:
        return {"status":"Failure"}, 500

def actualizar_coche(id, nombre, descripcion, precio, foto, marca):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE coches SET nombre=%s, descripcion=%s, precio=%s, foto=%s, marca=%s WHERE id=%s",
                (nombre, descripcion, precio, foto, marca, id)
            )
            ret = {"status":"OK"} if cursor.rowcount else {"status":"Failure"}
        conexion.commit()
        conexion.close()
        return ret, 200
    except:
        return {"status":"Failure"}, 500
