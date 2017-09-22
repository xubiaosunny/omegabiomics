#-*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class ServiceIndex(models.Model):
    description = RichTextUploadingField(verbose_name='内容',blank=True)
    class Meta:
        verbose_name = '科研服务主页'
        verbose_name_plural = '科研服务主页'



class FristItem(models.Model):
    name = models.CharField(verbose_name="一级标题",max_length=128)
    class Meta:
        verbose_name = '科研服务一级分类'
        verbose_name_plural = '科研服务一级分类'
    def __str__(self):
        return self.name


class SecondItem(models.Model):
    frist_item = models.ForeignKey(FristItem, verbose_name="一级标题")
    name = models.CharField(verbose_name='二级标题',max_length=128)
    class Meta:
        verbose_name = '科研服务二级目录'
        verbose_name_plural = '科研服务二级目录'
    def __str__(self):
        return '%s-%s' % (self.frist_item, self.name)


class ThirdItem(models.Model):
    second_item = models.ForeignKey(SecondItem, verbose_name='二级标题')
    name = models.CharField(verbose_name='内容标题',max_length=128)
    description = RichTextUploadingField(verbose_name='内容',blank=True)
    class Meta:
        verbose_name = '科研服务内容目录'
        verbose_name_plural = '科研服务内容目录'
    def __str__(self):
        return self.name