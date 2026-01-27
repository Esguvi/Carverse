from bd import obtener_conexion
import sys
import datetime as dt




def insertar_comentario(email, descripcion):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO comentarios(email, descripcion) VALUES ('"+ email +"','" + descripcion + "')")
            conexion.commit()
        conexion.close()
        ret={"status": "OK" }
        code=200
    except:
        ret={"status": "ERROR" }
        print("Excepcion al insertar un comentario", flush=True)
        code=500   
    return ret,code

def obtener_comentarios():
    comentariosjson=[]
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT email, descripcion FROM comentarios")
            comentarios = cursor.fetchall()
           
            
        conexion.close()
        code=200
    except Exception as e:
        print("Excepcion al consultar todas los comentarios", e, flush=True)
        code=500
    return comentarios,code