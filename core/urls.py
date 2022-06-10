from django.urls import path
from .views import index,somos,galeria,contacto,dogApi,login,mapa,noCuenta,form_del_producto,form_mod_producto,mostrar,form_producto

urlpatterns = [
    path('', index , name="index"),
    path('somos/',somos,name="somos"),
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto,name="contacto"),
    path('mapa/',mapa,name="mapa"),
    path('dogApi/',dogApi,name="dogApi"),
    path('login/',login,name="login"),
    path('noCuenta/',noCuenta,name="noCuenta"),
    path ('mostrar/', mostrar, name="mostrar"),
    path ('form_producto/', form_producto, name="form_producto"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),

]