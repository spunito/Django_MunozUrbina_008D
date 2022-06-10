# Generated by Django 4.0.5 on 2022-06-10 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaAnimal',
            fields=[
                ('idCategoriaA', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoriaA', models.CharField(max_length=50, verbose_name='Nombre de Categoria Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Animal',
            fields=[
                ('id_producto', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='id_producto')),
                ('descripcionP', models.CharField(max_length=60, verbose_name='Descripcion')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriaanimal', verbose_name='Categoria Animal')),
            ],
        ),
    ]
