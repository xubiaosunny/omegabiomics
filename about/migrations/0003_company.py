# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 08:14
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20170917_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='公司介绍')),
            ],
            options={
                'verbose_name': '公司介绍',
                'verbose_name_plural': '公司介绍',
            },
        ),
    ]
