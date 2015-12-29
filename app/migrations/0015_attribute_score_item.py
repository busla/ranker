# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20151206_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='score_item',
            field=models.ForeignKey(to='app.ScoreItem', blank=True, null=True),
        ),
    ]
