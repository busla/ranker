# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0007_scoresystem_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreitem',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', blank=True, verbose_name='Tags', help_text='A comma-separated list of tags.'),
        ),
    ]
