# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_scoreitem_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeitem',
            name='partitipation',
            field=models.BooleanField(default=False),
        ),
    ]
