from django.contrib import admin
from .models import *
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'title')


class PartnerAdmin(admin.ModelAdmin):
    list_display=('id', 'name',)


class NewsAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'date')


class CompanyAdmin(admin.ModelAdmin):
    list_display=('id',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Company, CompanyAdmin)