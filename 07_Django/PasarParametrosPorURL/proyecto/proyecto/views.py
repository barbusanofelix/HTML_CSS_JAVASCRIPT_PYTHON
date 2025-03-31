
from django.http import HttpResponse  #* PASO 1: Importamos el metodo djngo.http de la clase HttpResponse. 
import datetime

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista: En realidad es un metodo o funcion.
#* PASO 2: CREAMOS LA FUNCION QUE SERA LA VISTA, CON PARAMETRO request. 
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento de la vista.
    return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")    #* PASO 3: EL RETORNO ES UNA RESPUESTA HttpResponse.

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento de la vista.
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django, EN ROJO. =)</p>")    #* PASO 3: EL RETORNO ES UNA RESPUESTA HttpResponse.

def categoria_edad(request,edad):
    if edad>18:
        if edad>60:
            categoria="Tercera edad"
        else:
            categoria="Adulto"
    else:
        if edad<=10:
            categoria="Infantil"
        else:
            categoria="Adolecente"
    resultado= "<h1> La categoria de la edad es : %s </h1>" %categoria    # %s es un referencia a un string.0 %s se reemplaza con el valor de la variable categoria
    
    return HttpResponse(resultado)                       

def obtener_momento_actual(request):
    # resultado="<h1>El momento actual es  {0} </h1>" .format(datetime.datetime.now())
    resultado="<h1>El momento actual es  {0} </h1>" .format(datetime.datetime.now().strftime("%A %d/ %m /%Y %H:%M:%S"))
    return HttpResponse(resultado)