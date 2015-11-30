# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151129_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreitem',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', blank=True, always_update=True, editable=False),
        ),
        migrations.AddField(
            model_name='scoreitem',
            name='title',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
    ]
