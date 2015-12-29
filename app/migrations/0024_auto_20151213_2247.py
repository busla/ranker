# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20151213_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='club',
            field=models.ForeignKey(null=True, to='app.Club', blank=True),
        ),
        migrations.AddField(
            model_name='results',
            name='athlete_club',
            field=models.ForeignKey(null=True, to='app.Club', blank=True),
        ),
    ]
