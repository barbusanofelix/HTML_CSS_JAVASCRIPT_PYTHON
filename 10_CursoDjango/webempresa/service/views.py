from django.shortcuts import render
from .models import Service

# Create your views here.
def servicios_services(request):
    services= Service.objects.all()                # Recupera todos los Service de la base de datos y los guarda en services
    return render(request,"service/services.html", {'services':services})  

"""
'services' : Un diccionario de contexto. Este diccionario contiene datos que estarán disponibles dentro de la plantilla HTML. 
En este caso, estás pasando una clave llamada 'services' cuyo valor es la lista de objetos Service que recuperaste de la 
base de datos. Dentro de la plantilla services.html, podrás acceder a esta lista utilizando la variable 

{{ services }}.

"""