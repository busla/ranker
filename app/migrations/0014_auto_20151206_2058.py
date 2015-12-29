# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_attribute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scoresystem',
            options={'verbose_name': 'Score System', 'ordering': ['title'], 'verbose_name_plural': 'Score Systems'},
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='results',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='tags',
        ),
    ]
