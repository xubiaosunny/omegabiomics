# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 15:51
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FristItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='一级标题')),
            ],
            options={
                'verbose_name': '一级分类',
                'verbose_name_plural': '一级分类',
            },
        ),
        migrations.CreateModel(
            name='SecondItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='二级标题')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.FristItem')),
            ],
            options={
                'verbose_name': '二级目录',
                'verbose_name_plural': '二级目录',
            },
        ),
        migrations.CreateModel(
            name='ThirdItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='内容标题')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='内容')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.SecondItem')),
            ],
            options={
                'verbose_name': '内容目录',
                'verbose_name_plural': '内容目录',
            },
        ),
    ]
