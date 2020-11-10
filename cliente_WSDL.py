# Ejemplo basico de consumo de WSDL con suds
# ejemplo base del ejemplo http://www.rz0r.net/2011/07/consumir-web-services-soap-facil-con-python-suds/
# como instalar suds con pip https://bitbucket.org/jurko/suds


from suds.client import Client #agregar la libreria de suds, con el metodo client

url = 'http://127.0.0.1/wsdl_user/wsGetAllUsers.php?wsdl' # path del wsdl
client = Client(url)  # parseo de la la url a la funcion client
result = client.service.consultaUsuarios() # instanciar el metodo a invocar en este caso "consultaUsuarios" que requiere un dato vacio
#print(result) # en este caso el servicio retorna un array
for i in range(0,len(result)): # accediendo al array del resultado
    value = result[i]
    print (value)

#print(result[0])