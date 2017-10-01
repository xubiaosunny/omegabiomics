#-*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Carousel(models.Model):
    img = models.ImageField(upload_to='carousel/%Y/%m/%d',verbose_name='图片')
    link = models.URLField(verbose_name="链接地址", null=True, blank=True)
    display = models.BooleanField(default=True, verbose_name='是否显示')
    class Meta:
        ordering = ["-id",]
        verbose_name = 'Banner配置'
        verbose_name_plural = 'Banner配置'


class CompanyIndex(models.Model):
    introduction = RichTextField(verbose_name='关于奥美德诺')
    class Meta:
        verbose_name = '关于奥美德诺'
        verbose_name_plural = '关于奥美德诺'


class ModuleImg(models.Model):
    img = models.ImageField(upload_to='module/%Y/%m/%d', verbose_name='图片')
    link = models.URLField(verbose_name="链接地址", null=True, blank=True)
    class Meta:
        verbose_name = '首页三图片（只能填三个）'
        verbose_name_plural = '首页三图片（只能填三个）'


class Keyword(models.Model):
    name = models.CharField(verbose_name='关键词', max_length=255)
    class Meta:
        verbose_name = '网站关键词'
        verbose_name_plural = '网站关键词'
