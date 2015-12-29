# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20151207_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreitem',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
