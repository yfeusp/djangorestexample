# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.IntegerField(unique=True, verbose_name='id')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(choices=[('Angiolog\xeda', 'Angiolog\xeda'), ('Cardiolog\xeda', 'Cardiolog\xeda'), ('Pediatr\xeda', 'Pediatr\xeda'), ('Reumatolog\xeda', 'Reumatolog\xeda'), ('Urolog\xeda', 'Urolog\xeda')], max_length=12)),
            ],
            options={
                'ordering': ['nombre', 'apellidos'],
            },
        ),
    ]