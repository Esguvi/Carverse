from bd import obtener_conexion
import sys
import datetime as dt

def login_usuario(email,password):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT name FROM usuarios WHERE email = '" + email +"' and password= '" + password + "'")
            email = cursor.fetchone()
            
            if email is None:
                ret = {"status": "ERROR","mensaje":"Usuario/password erroneo" }
            else:
                ret = {"status": "OK" }
        code=200
        conexion.close()
    except:
        print("Excepcion al validar al email", flush=True)   
        ret={"status":"ERROR"}
        code=500
    return ret,code

def alta_usuario(email,password,name):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT name FROM usuarios WHERE email = %s",(email,))
            email = cursor.fetchone()
            if email is None:
                cursor.execute("INSERT INTO usuarios(email,password,name) VALUES('"+ email +"','"+  password+"','"+ name+"')")
                if cursor.rowcount == 1:
                    conexion.commit()
                    ret={"status": "OK" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje":"Usuario ya existe" }
                code=200
        conexion.close()
    except:
        print("Excepcion al registrar al email", flush=True)   
        ret={"status":"ERROR"}
        code=500
    return ret,code    

def logout():
    return {"status":"OK"},200

