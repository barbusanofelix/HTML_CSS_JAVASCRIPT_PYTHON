from django.db import models

# Create your models here.
class Link(models.Model):
    Key=models.SlugField(verbose_name='Nombre Clave', max_length=100, unique=True)
    name=models.CharField(max_length=200, verbose_name='Red Social')
    url=models.URLField(max_length=200, verbose_name='Enlace', blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    # OJO: ES UNA SUBCLASE PUES ESTA IDENTADA DENTRO DE PROJECT   : OJO , QUE ES UNA SUBCLASE
    class Meta:                                 # Una clase de metadatos
        verbose_name='enlace'                 # Nombre en singular
        verbose_name_plural='enlaces'         # Nombres en prural
        ordering=["name"]                    # ordenar ascendeste( por defecto) 
    
    def __str__(self):
        return self.name