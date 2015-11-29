# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('ssn', models.CharField(null=True, max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'Athlete',
                'verbose_name_plural': 'Athletes',
                'ordering': ['ssn'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('athlete', models.ForeignKey(to='app.Athlete')),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
                'ordering': ['athlete'],
            },
        ),
        migrations.CreateModel(
            name='ScoreItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('place', models.IntegerField(null=True, blank=True)),
                ('points', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(null=True, to='app.Category', blank=True)),
                ('score', models.ManyToManyField(blank=True, to='app.ScoreItem')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(null=True, blank=True)),
                ('date', models.DateField()),
                ('score_system', models.ManyToManyField(blank=True, to='app.ScoreSystem')),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='tournament',
            field=models.ForeignKey(to='app.Tournament'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='avatar',
            field=models.ForeignKey(null=True, to='app.Image', blank=True),
        ),
    ]
