
from django.http import HttpResponse  #* PASO 1: Importamos el metodo djngo.http de la clase HttpResponse. 

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista: En realidad es un metodo o funcion.
#* PASO 2: CREAMOS LA FUNCION QUE SERA LA VISTA, CON PARAMETRO request. 
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento de la vista.
    return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")    #* PASO 3: EL RETORNO ES UNA RESPUESTA HttpResponse.

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento de la vista.
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django, EN ROJO. =)</p>")    #* PASO 3: EL RETORNO ES UNA RESPUESTA HttpResponse.