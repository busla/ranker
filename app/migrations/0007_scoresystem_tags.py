# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0006_scoresystem_scale'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoresystem',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.'),
        ),
    ]
