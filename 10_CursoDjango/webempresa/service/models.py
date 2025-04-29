from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=200, verbose_name='Titulo')
    subtitle=models.CharField(max_length=200, verbose_name='Subtitulo')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(verbose_name='Imagen', upload_to='services')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    # OJO: ES UNA SUBCLASE PUES ESTA IDENTADA DENTRO DE PROJECT   : OJO , QUE ES UNA SUBCLASE
    class Meta:                                 # Una clase de metadatos
        verbose_name='servicio'                 # Nombre en singular
        verbose_name_plural='servicios'         # Nombres en prural
        ordering=["-created",]                   # el - es para ordenar de mayor a menor.
    
    def __str__(self):
        return self.title    