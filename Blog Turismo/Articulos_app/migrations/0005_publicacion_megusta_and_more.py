# Generated by Django 4.2.2 on 2023-07-28 13:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articulos_app', '0004_rename_post_comentario_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='megusta',
            field=models.ManyToManyField(blank=True, related_name='articulos_megusta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
