# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_scoreitem_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='result',
            field=models.ForeignKey(to='app.Results', null=True, blank=True),
        ),
    ]
