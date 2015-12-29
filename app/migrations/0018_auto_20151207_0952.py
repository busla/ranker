# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_attribute_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='score_item',
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_items',
            field=models.ForeignKey(blank=True, null=True, to='app.AttributeItem'),
        ),
    ]
