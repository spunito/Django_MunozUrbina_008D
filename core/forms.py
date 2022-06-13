from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import CategoriaAnimal,Productos_Animal

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Productos_Animal
        fields = ['id_producto', 'descripcionP', 'marca', 'imagen','categoria']
        labels ={
            'id_producto': 'ID del producto', 
            'descripcionP' :'Descripcion Producto', 
            'marca': 'Marca', 
            'imagen':'Imagen',
            'categoria': 'Categoría',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',
                    
                    
                }
            ), 
            'descripcionP': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'id': 'imagen'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

 