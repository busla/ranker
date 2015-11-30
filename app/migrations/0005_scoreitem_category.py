# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151130_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, to='app.Category'),
        ),
    ]
