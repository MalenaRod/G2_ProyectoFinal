# Generated by Django 4.2.2 on 2023-07-26 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_articulos')),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_articulos', to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articulos', to='Articulos_app.categoria')),
            ],
            options={
                'ordering': ['fecha_publicacion'],
            },
        ),
    ]
