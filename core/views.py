from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productos_Animal
from .forms import ProductoForm

# Create your views here.
TEMPLATES_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")
def somos(request):
    return render(request ,"somos.html")
def galeria(request):
    return render(request ,"galeria.html")
def contacto(request):
    return render(request,"contacto.html")
def mapa(request):
    return render(request ,"maps.html")
def dogApi(request):
    return render(request,"dogsAPI.html")
def login(request):
    return render(request,"login.html")
def noCuenta(request):
    return render(request , "no_cuenta.html")

#Termino Templates normales - Inicia Templates CRUD

def mostrar(request):
    productos = Productos_Animal.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)

def form_producto(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('index')
    else:
        producto_form= ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})


def form_mod_producto(request, id): 
    producto = Productos_Animal.objects.get(id_producto=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_mod_producto.html', datos )

def form_del_producto(request, id):
    producto = Productos_Animal.objects.get(id_producto=id)
    producto.delete()
    return redirect('mostrar')


