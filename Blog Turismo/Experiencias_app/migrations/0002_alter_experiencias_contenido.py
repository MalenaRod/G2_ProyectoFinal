# Generated by Django 4.2.2 on 2023-08-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Experiencias_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencias',
            name='contenido',
            field=models.TextField(max_length=500),
        ),
    ]
