from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Team(models.Model):
    img = models.ImageField(upload_to='team/%Y/%m/%d',verbose_name='照片')
    name = models.CharField(verbose_name="名字", null=True, max_length=255)
    title = models.CharField(verbose_name="职称", null=True, blank=True, max_length=255)
    description = models.TextField(default=True, verbose_name='描述')
    class Meta:
        verbose_name = '团队成员'
        verbose_name_plural = '团队成员'


class Partner(models.Model):
    img = models.ImageField(upload_to='partner/%Y/%m/%d',verbose_name='logo')
    name = models.CharField(verbose_name="名称", null=True, max_length=255)
    class Meta:
        verbose_name = '合作伙伴'
        verbose_name_plural = '合作伙伴'


class News(models.Model):
    img = models.ImageField(upload_to='news/%Y/%m/%d',verbose_name='标题图')
    name = models.CharField(verbose_name="文章标题", null=True, max_length=255)
    content = RichTextUploadingField(verbose_name='内容', blank=True)
    date = models.DateField()
    class Meta:
        ordering = ['-date', '-id']
        verbose_name = '新闻动态'
        verbose_name_plural = '新闻动态'