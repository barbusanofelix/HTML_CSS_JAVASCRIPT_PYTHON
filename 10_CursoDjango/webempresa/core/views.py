from django.shortcuts import render, HttpResponse



# Create your views here.
def inicio_home(request):
    return render(request, 'core/home.html')


def historia_about(request):
    return render(request,"core/about.html")


def visitanos_store(request):
    return render(request,"core/store.html")


def blog_blog(request):
    return render(request,"core/blog.html")


