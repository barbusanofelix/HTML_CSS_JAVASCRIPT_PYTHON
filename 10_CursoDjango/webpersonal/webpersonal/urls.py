"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio__views
from django.conf import settings                            #Hace que las variables MEDIA_URL='/MEDIA/' y MEDIA_ROOT sean accesibles aqui

urlpatterns = [
    path('',core_views.home, name='home'),                      # '' significa que lalmaremos este viwes.home con solo http://127.0.0.1:8000/
    path('about-me/', core_views.about, name='about'),          # about-me/  es lo que escribimos luego de http://127.0.0.1:8000/about-me/
    path('contact/', core_views.contact,name='contact'),
    path('portafolio/',portfolio__views.portfolio,name='portfolio'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # permite cargar los archivos statics ( media )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
