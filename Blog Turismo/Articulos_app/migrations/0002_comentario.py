# Generated by Django 4.2.2 on 2023-07-26 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articulos_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Articulos_app.publicacion')),
            ],
        ),
    ]
