from django.urls import path
from .views import index,somos,galeria,contacto,dogApi,login,mapa,noCuenta

urlpatterns = [
    path('', index , name="index"),
    path('somos/',somos,name="somos"),
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto,name="contacto"),
    path('mapa/',mapa,name="mapa"),
    path('dogApi/',dogApi,name="dogApi"),
    path('login/',login,name="login"),
    path('noCuenta/',noCuenta,name="noCuenta"),

]