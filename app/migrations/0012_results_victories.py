# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151202_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='victories',
            field=models.IntegerField(default=0),
        ),
    ]
