from django.shortcuts import render
from .models import Usuario, Producto, Venta
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        return render(request, "myapp/formulario.html")
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

def login(request):
    if request.method=="POST":
        #Corresponde al formulario
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"myapp/index.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"myapp/login.html",context)
    else:
        #Corresponde a redireccionar
        context = {
        }
        return render(request,"myapp/login.html",context)



def tienda (request):
    return render(request, 'myapp/tienda.html')