# Generated by Django 4.2.2 on 2023-07-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/articulos'),
        ),
    ]