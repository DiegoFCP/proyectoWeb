from django.shortcuts import render
from .models import Usuario, Producto, Venta
from .forms import UsuarioForm

# Create your views here.

def index (request):
    context={}
    return render(request, 'myapp/index.html',context)
    
def about (request):
    return render(request, 'myapp/about.html')

def galeria (request):
    return render(request, 'myapp/galeria.html')

def formulario (request):
    if request.method != 'POST':
        usuario = Usuario.objects.all()
        context = {
            "usuario": Usuario,
        }
        return render(request, "myapp/formulario.html", context)
    else:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        contraseña = request.POST["contraseña"]
        direccion = request.POST["direccion"]
        activo = True

        obj = Usuario.objects.create(
            nombre = nombre,
            apellido = apellido,
            correo = correo,
            contraseña = contraseña,
            direccion = direccion,
            activo = activo
           )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "myapp/formulario.html", context)

def noticias (request):
    return render(request, 'myapp/noticias.html')

def api (request):
    return render(request, 'myapp/api.html')

def login (request):
    return render(request, 'myapp/login.html')

def tienda (request):
    return render(request, 'myapp/tienda.html')