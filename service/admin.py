from django.contrib import admin

# Register your models here.
from .models import *


class FristItemAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


class SecondItemAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


class ThirdItemAdmin(admin.ModelAdmin):
    list_display = ('id','name',)



admin.site.register([FristItem],FristItemAdmin)
admin.site.register([SecondItem],SecondItemAdmin)
admin.site.register([ThirdItem],ThirdItemAdmin)


class ServiceIndexAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register([ServiceIndex],ServiceIndexAdmin)
