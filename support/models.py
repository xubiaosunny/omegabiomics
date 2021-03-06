from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Support(models.Model):
    name = models.CharField(verbose_name='名称',max_length=128)
    description = RichTextUploadingField(verbose_name='内容',blank=True)
    class Meta:
        verbose_name = '产品中心'
        verbose_name_plural = '产品中心'
    def __str__(self):
        return self.name