# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151201_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scoreitem',
            options={'ordering': ['place'], 'verbose_name_plural': 'Score Items', 'verbose_name': 'Score Item'},
        ),
    ]
