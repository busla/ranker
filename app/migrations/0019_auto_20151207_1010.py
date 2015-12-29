# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151207_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='attribute_items',
            new_name='attribute_item',
        ),
        migrations.RemoveField(
            model_name='attributeitem',
            name='value',
        ),
        migrations.AddField(
            model_name='scoreitem',
            name='attribute_item',
            field=models.ForeignKey(null=True, blank=True, to='app.AttributeItem'),
        ),
    ]
