from django.contrib import admin
from .models import Service 


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):           # Esto permite que los campos de solo lectura se muestren al crear esta clase si la acompañamos con admin.site.register
    readonly_fields=('created', 'updated')  
    
admin.site.register(Service, ServiceAdmin) 
     