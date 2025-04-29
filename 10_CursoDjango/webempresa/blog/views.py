from django.shortcuts import render,get_object_or_404
from .models import Post           # Importamos el modelo a la vista
from .models import Category

# Create your views here.
def blog_blog(request):
    posts=Post.objects.all()                  # Recupera todos los registros de Post y los guarda como Query Set es post
    return render(request,"blog/blog.html", {'posts':posts})  #Le pasamos el Query Set 

def category(request, category_id):
    category=get_object_or_404(Category,id=category_id)
    return render(request, 'blog/category.html', {'category':category})

