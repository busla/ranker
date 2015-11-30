# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_scoreitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresystem',
            name='scale',
            field=models.FloatField(default=1),
        ),
    ]
