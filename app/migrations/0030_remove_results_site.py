# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20151220_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='site',
        ),
    ]
