# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170914_2336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-id'], 'verbose_name': 'Banner配置', 'verbose_name_plural': 'Banner配置'},
        ),
    ]
