# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_movements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movements',
            new_name='Movement',
        ),
    ]
