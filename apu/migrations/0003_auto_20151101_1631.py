# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apu', '0002_apuesta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apuesta',
            new_name='RegApuesta',
        ),
    ]
