# Generated by Django 5.1 on 2024-12-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('gerente', models.CharField(max_length=100)),
                ('capacidad', models.PositiveSmallIntegerField()),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
