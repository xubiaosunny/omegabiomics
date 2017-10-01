from django.contrib import admin
from home.models import *
# Register your models here.


class CarouselAdmin(admin.ModelAdmin):
    list_display=('id','img','link','display')


admin.site.register(Carousel, CarouselAdmin)

class CompanyIndexAdmin(admin.ModelAdmin):
    list_display=('id',)


admin.site.register(CompanyIndex, CompanyIndexAdmin)


class ModuleImgAdmin(admin.ModelAdmin):
    list_display=('id',)


admin.site.register(ModuleImg, ModuleImgAdmin)


class KeywordAdmin(admin.ModelAdmin):
    list_display=('id', 'name',)


admin.site.register(Keyword, KeywordAdmin)
