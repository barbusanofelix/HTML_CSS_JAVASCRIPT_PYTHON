# Direcciones URL de vistas de core

from django.urls import path
from core import views as core_views


urlpatterns = [
    
    # Vistas de app core
    path('',core_views.inicio_home, name='home'), 
    path('about/',core_views.historia_about, name='about'), 
    path('store/',core_views.visitanos_store, name='store'), 
    path('contact/',core_views.contacto_contact, name='contact'),  
    path('sample/',core_views.sample_sample, name='sample'),
    
]
