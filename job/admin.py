from django.contrib import admin
from .models import *
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title',)


admin.site.register([Job], JobAdmin)