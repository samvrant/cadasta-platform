# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spatial', '0004_auto_20160505_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spatialunit',
            old_name='geometry',
            new_name='extent',
        ),
    ]
