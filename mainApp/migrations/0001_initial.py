# Generated by Django 4.0.6 on 2022-07-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('subtitulo', models.CharField(max_length=70)),
                ('autor', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
