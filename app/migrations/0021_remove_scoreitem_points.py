# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_scoreitem_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreitem',
            name='points',
        ),
    ]
