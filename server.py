import bottle
#import time
import pymysql
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '' 
DB_NAME = 'bdpython'

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    conn = pymysql.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
    print (data)
    return data


#@bottle.get('/')
#def foo():
    #return "<html></html><head></head><title>pythonweb</title><body><em>Hola Mundo</em></body>"

#@bottle.get("/time")
#def foo1():
    #return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

@bottle.get('/usuarios')
def foo():
    query = "SELECT id_usuario, usr_nombre, usr_correo  FROM sys_usuarios ORDER BY 1 " 
    result = run_query(query) 
    return "<html></html><head></head><title>pythonweb</title><body><em>"+str(result)+"</em></body>"



bottle.run(host = "localhost", port = 3000)