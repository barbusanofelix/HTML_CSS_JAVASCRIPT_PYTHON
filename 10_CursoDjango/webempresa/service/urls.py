
from django.urls import path
from service import views as serv_views


urlpatterns = [
    
# vistas de app service
     path('',serv_views.servicios_services, name='services'),   # path lo iniciamos en raiz=' ' porque ya la URL vendra con service/
     
]     