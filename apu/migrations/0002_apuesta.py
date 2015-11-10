# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipoa', models.CharField(max_length=50)),
                ('equipob', models.CharField(max_length=50)),
                ('capital', models.IntegerField()),
                ('victoria', models.CharField(max_length=1)),
                ('apostador', models.ForeignKey('Persona')),
            ],
        ),
    ]
