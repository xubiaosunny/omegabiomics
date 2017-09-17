# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 16:20
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='news/%Y/%m/%d', verbose_name='标题图')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='文章标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='内容')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': '新闻动态',
                'verbose_name_plural': '新闻动态',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='partner/%Y/%m/%d', verbose_name='logo')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '合作伙伴',
                'verbose_name_plural': '合作伙伴',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='team/%Y/%m/%d', verbose_name='照片')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名字')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='职称')),
                ('description', models.TextField(default=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '团队成员',
                'verbose_name_plural': '团队成员',
            },
        ),
    ]
