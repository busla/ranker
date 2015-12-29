# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_attributeitem_partitipation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributeitem',
            old_name='partitipation',
            new_name='participation',
        ),
    ]
