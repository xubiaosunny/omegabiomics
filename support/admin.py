from django.contrib import admin
from .models import *
# Register your models here.


class SupportAdmin(admin.ModelAdmin):
    list_display = ('id','name',)



admin.site.register([Support], SupportAdmin)