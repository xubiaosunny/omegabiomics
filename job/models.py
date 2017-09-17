from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(verbose_name='职位',max_length=128)
    work_place = models.CharField(verbose_name='工作地点',max_length=128)
    duty = models.TextField(verbose_name='岗位职责')
    request = models.TextField(verbose_name='岗位要求')
    class Meta:
        verbose_name = '招贤纳士'
        verbose_name_plural = '招贤纳士'
    def __str__(self):
        return self.title