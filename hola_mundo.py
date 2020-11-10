
print ("Hola mundo")
#este es un comentario

nombre = 'Luis Rogelio'
apellido = 'Batres Guarneros'

strNombre = nombre+' '+apellido
print (strNombre)


#Operaciones matematicas con funciones

#definicion de funcion suma
def funSuma (a, b):
    c = a + b
    print (c) #imprime resultado
    #return c #retorna el resultado a la invocacion 

#definicion de funcion retorna
def funSumareturn (a, b):
    c = a + b
    return c


#definicion de funcion resta
def funResta (a, b):
    c = a - b
    print (c)

#definicion de funcion retorna
def funRestareturn (a, b):
    c = a - b
    return c        


#invoca funcion suma
a = 10
b = 15
funSuma(a, b)

#invocacion funcion resta
a = 10
b = 15
funResta(a, b)

#manejo de funciones multiples
a = 10
b = 25
d = 3
e = 1
c = funSumareturn(a, b)
f = funRestareturn(d, e)
print (c)
print (f)
g = c * f
#variante
h = funSumareturn(a, b) * funRestareturn(d, e) 
print (g)
print (h)

#listas
lista = [1, 2, 3, 4, 5]
print (lista)
print (lista[1])
liststring = ['luis', 'rogelio', 'batres']
print(liststring[1])

#recorer elementos de un array  for
autos = ['bocho', 'golf', 'gol', 'versa']
num = range(len(autos)) #largo del array
print (num)
i = 0;

for marca in autos:
    print ('marc:', marca)


#conetar con base de datos
#Se requiere instalar los controladores de pymysql
#por tal motivo descargar de https://github.com/PyMySQL/PyMySQL/
# e instalar desde consola CMD de windows: 
#python setup.py build
#python setup.py install

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
 
    return data

#ejecuta consulta select
query = "SELECT id_usuario, usr_nombre, usr_correo  FROM sys_usuarios ORDER BY 1 " 
print (query)
result = run_query(query) 
print (result)

#ejecuta consulta insert
id_usuario = "4"
usr_nombre = "adrian de aguilar"
usr_correo = "aaguilarAmail.com"

#query = "INSERT INTO sys_usuarios (id_usuario) VALUES ('%s')" % id_usuario
query = "INSERT INTO sys_usuarios (id_usuario, usr_nombre, usr_correo) VALUES ('" + str(id_usuario) + "' , '" + str(usr_nombre) + "' , '" + str(usr_correo) + "')" 
print (query)
#run_query(query)
print ('#######################################################################################')
#para convertir un PDF a binario se requiere una libreria externa
#python magic que la descargas de: https://github.com/ahupp/python-magic
#para instalarla se requiere desde CMD de windows:
#python setup.py build
#python setup.py install
#import magic
#magic.from_file("HOLAMUNDO.pdf") #'PDF document, version 1.2'
#magic.from_buffer(open("HOLAMUNDO.pdf").read(1024)) #'PDF document, version 1.2'
#magic.from_file("HOLAMUNDO.pdf", mime=True) #'application/pdf'


#manejo de datos en base64_encode 
#libreria base64-3.3.3-2 que la descargas de:https://pypi.python.org/pypi/micropython-base64/
#para instalarla se requiere desde CMD de windows:
#python setup.py build
#python setup.py install
#import base64
#encoded = base64.b64encode('data to be encoded')

############################################################################3
#tuplas y listas
#Una lista puede ser alterada, no así una tupla.
#Una tupla puede ser utilizada como clave en un diccionario, no así una lista.
#Una tupla consume menos espacio que una lista.


tupla = (1,2,3,4,5,6,7,8,9,10)
lista = [1,2,3,4,5,6,7,8,9,10]
 
print(tupla.__sizeof__()) # 52 bytes
print(lista.__sizeof__()) # 60 bytes

tupla1000 = tuple(range(1000))
lista1000 = list( range(1000))
 
print(tupla1000.__sizeof__()) # 4012
print(lista1000.__sizeof__()) # 4544

#Direccionarios

d = {"Love Actually ": "Richard Curtis","Kill Bill": "Tarantino","Amélie": "Jean-Pierre Jeunet"}
print (d)

#sentenia condicional if
#debe de tener identacion

fav = "mundogeek.net"
if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
    print ("Gracias")
else:
    print ("Vaya, que lástima")

numero = 10

if numero < 0:
    print ("Negativo")
elif numero > 0:
    print ("Positivo")
else:
    print ("Cero")  