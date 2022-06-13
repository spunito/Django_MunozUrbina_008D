from django.db import models

# Create your models here.

class CategoriaAnimal(models.Model):
    idCategoriaA = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoriaA=models.CharField(max_length=50, verbose_name='Nombre de Categoria Animal')

    def __str__(self): 
        return self.nombreCategoriaA


class Productos_Animal (models.Model): 
    id_producto = models.CharField(primary_key=True, max_length=6, verbose_name='id_producto')
    descripcionP= models.CharField(max_length=60, verbose_name='Descripcion')
    marca= models.CharField(max_length=20, verbose_name='Marca') 
    imagen =models.ImageField(upload_to="productos",null=True)
    categoria = models.ForeignKey(CategoriaAnimal, on_delete=models.CASCADE, verbose_name='Categoria Animal')


    def __str__(self):
        return self.descripcionP

        