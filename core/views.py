from django.shortcuts import render
from django.http import HttpResponse

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


