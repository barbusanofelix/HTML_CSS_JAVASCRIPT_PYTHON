from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()                # projects es una lista que recibira todos los objetos Projects    
    return render(request,'portfolio/portafolio.html', {'projects':projects})    # devuelve a la lista el diccionario
