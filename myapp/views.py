from django.shortcuts import render

# Create your views here.

def index (request):
    context={}
    return render(request, 'myapp/index.html',context)
    
def about (request):
    return render(request, 'myapp/about.html')

def galeria (request):
    return render(request, 'myapp/galeria.html')

def formulario (request):
    return render(request, 'myapp/formulario.html')

def noticias (request):
    return render(request, 'myapp/noticias.html')

def api (request):
    return render(request, 'myapp/api.html')

def login (request):
    return render(request, 'myapp/login.html')