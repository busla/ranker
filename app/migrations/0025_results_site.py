# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('app', '0024_auto_20151213_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='site',
            field=models.ForeignKey(to='sites.Site', default=1),
            preserve_default=False,
        ),
    ]
