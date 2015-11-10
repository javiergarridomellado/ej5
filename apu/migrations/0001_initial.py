# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9)),
                ('pais', models.CharField(max_length=20)),
                ('equipo', models.CharField(max_length=10)),
                ('hobbies', models.TextField(max_length=200)),
                ('fondo' ,  models.IntegerField()),
            ],
        ),
    ]
