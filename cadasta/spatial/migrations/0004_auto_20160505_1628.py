# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spatial', '0003_auto_20160505_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spatialunit',
            name='relationships',
            field=models.ManyToManyField(related_name='relationships_set', through='spatial.SpatialUnitRelationship', to='spatial.SpatialUnit'),
        ),
    ]
