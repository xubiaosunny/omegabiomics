# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20170916_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thirditem',
            old_name='second_system',
            new_name='second_item',
        ),
    ]
