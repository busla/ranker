# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0012_results_victories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.FloatField(default=0)),
                ('results', models.ForeignKey(to='app.Results', blank=True, null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True, through='taggit.TaggedItem')),
            ],
        ),
    ]
