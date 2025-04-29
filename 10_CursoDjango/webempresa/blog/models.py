from django.utils import timezone      # Para poder acceder a zona horaria y hacer uso de timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models Category
class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
     # OJO: ES UNA SUBCLASE PUES ESTA IDENTADA DENTRO DE CATEGORY   : OJO , QUE ES UNA SUBCLASE
     # Esta se usa para traducir a español la aparicion de las referencias a category 
    class Meta:                                 # Una clase de metadatos
        verbose_name='categoria'                 # Nombre en singular
        verbose_name_plural='categorias'         # Nombres en prural
        ordering=["-created",]                   # el - es para ordenar de mayor a menor.
    
    def __str__(self):
        return self.name   
    
class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name='Titulo')
    content=models.TextField(verbose_name='Contenido')  # Este campo no tiene limite
    published=models.DateTimeField(verbose_name='Publicacion', default=timezone.now)
    # null=True, blank=True hacen el campo imagen como opcional ( no obligatorio)
    image=models.ImageField(verbose_name='imagen',upload_to='blog', null=True, blank=True)
    # Django gestiona los usuarios con model user
    author=models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)     # Si se elimina el usuario se elimina el Post
    categories=models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")             # Cada Post puede tener varias categorias.
    created=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')   # No cambia
    updated=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')  # Cambia al actualizar
    
    class Meta:                                 # Una clase de metadatos
        verbose_name='entrada'                 # Nombre en singular
        verbose_name_plural='entradas'         # Nombres en prural
        ordering=["-created",]                   # el - es para ordenar de mayor a menor.
    
    def __str__(self):
        return self.title