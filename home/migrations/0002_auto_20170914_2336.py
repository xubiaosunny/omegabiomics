# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['display', '-id'], 'verbose_name': 'Banner配置', 'verbose_name_plural': 'Banner配置'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='display',
            field=models.BooleanField(default=True, verbose_name='是否显示'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='链接地址'),
        ),
    ]
