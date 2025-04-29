from django.contrib import admin
from .models import Category, Post  # Importamos los 2 modelos


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('name','id')
    
class PostAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')
     list_display=('title', 'author', 'published','content','postcategories')
     ordering=('title',)
     search_fields=('title','author__username', 'categories__name')
     date_hierarchy='published'
     list_filter=('author','categories')
     
     def postcategories(self,object):
         return ", ".join([c.name for c in object.categories.all().order_by("name")])
     
     postcategories.short_description="Categorias"
     
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
         