# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151130_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events', 'ordering': ['-date']},
        ),
    ]
