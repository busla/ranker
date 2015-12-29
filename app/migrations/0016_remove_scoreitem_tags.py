# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_attribute_score_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreitem',
            name='tags',
        ),
    ]
