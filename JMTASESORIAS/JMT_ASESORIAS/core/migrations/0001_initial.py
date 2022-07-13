# Generated by Django 4.0.4 on 2022-07-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('rol', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasacion',
            fields=[
                ('rut_propietario', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('propietario', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('documentacion', models.BinaryField()),
            ],
            options={
                'db_table': 'tasacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.BigIntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
