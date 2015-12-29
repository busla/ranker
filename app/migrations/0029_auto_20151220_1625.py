# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20151220_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='club',
            field=models.ManyToManyField(to='app.Club', related_name='clubs', blank=True),
        ),
    ]
