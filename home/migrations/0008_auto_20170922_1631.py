# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170922_1615'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='CompanyIndex',
        ),
    ]
