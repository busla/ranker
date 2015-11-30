# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_scoreitem_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreitem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='scoresystem',
            name='tags',
        ),
    ]
