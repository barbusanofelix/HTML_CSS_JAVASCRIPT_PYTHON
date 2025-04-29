from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):           # Esto permite que los campos de solo lectura se muestren al crear esta clase si la acompañamos con admin.site.register
    readonly_fields=('created', 'update')  
    
admin.site.register(Project, ProjectAdmin)      # Aqui de debe registrar ProjectAdmin para que se vean los campos.
