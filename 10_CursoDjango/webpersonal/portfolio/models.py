from django.db import models

# Create your models here.

class Project(models.Model):                  # Siempre hereda de models.Model que representa una tabla en la bd
    # Nombre de los campos y el tipo de dato
    title = models.CharField(max_length=200, verbose_name='Titulo')              # Un campo de cadena de caracteres
    description=models.TextField(verbose_name='Descripcion')          # Un campo de caracteres largos...campo de texto
    image =models.ImageField(verbose_name='Imagen',upload_to='project')              # Tipo imagen
    link=models.URLField(blank=True, null=True, verbose_name='Enlace')
    created=models.DateField(auto_now_add=True,verbose_name='Creado')     # Tipo fecha , donde se añadira la fecha/ hora al momento de creacion de una instancia
    update=models.DateField(auto_now=True,verbose_name='Actualizado')          # Tipo fecha, donde se registra la modifiacion, al modificar la instancia del Project
    
    # OJO: ES UNA SUBCLASE PUES ESTA IDENTADA DENTRO DE PROJECT   : OJO , QUE ES UNA SUBCLASE
    class Meta:                                 # Una clase de metadatos
        verbose_name='proyecto'                 # Nombre en singular
        verbose_name_plural='proyectos'         # Nombres en prural
        ordering=["-created",]                   # el - es para ordenar de mayor a menor.
    
    def __str__(self):
        return self.title