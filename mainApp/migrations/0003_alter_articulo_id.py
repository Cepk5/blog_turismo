# Generated by Django 4.0.6 on 2022-08-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_articulo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]